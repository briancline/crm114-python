import os
import string

CRM_BINARY = 'crm'

CLASSIFICATION_TYPE = '<osb unique microgroom>'
CLASSIFICATION_EXT = '.css'

LEARN_CMD = " '-{ learn %s ( %s ) }'"
CLASSIFY_CMD = " '-{ isolate (:stats:);" \
               " classify %s ( %s ) (:stats:);" \
               " match [:stats:] (:: :best: :prob:)" \
               " /Best match to file .. \(%s\/([[:graph:]]+)\\%s\)" \
               " prob: ([0-9.]+)/;" \
               " output /:*:best:\\t:*:prob:/ }'"


class Classifier:
    def __init__(self, path, categories=None):
        """ Wrapper class for the CRM-114 Discriminator. """
        self.categories = categories if categories else []
        self.path = path
        self.create_files()

    # learn the classifier what category some new text is in
    def learn(self, category, text):
        """ Feed the classifier some new text and a known classification for
        it, in order to improve subsequent categorizations. """

        command = CRM_BINARY + (LEARN_CMD % (CLASSIFICATION_TYPE,
                                             os.path.join(self.path, category +
                                                          CLASSIFICATION_EXT)))

        pipe = os.popen(command, 'w')
        pipe.write(text)
        pipe.close()

    def classify(self, text):
        """ Instructs the classifier to categorize the text, and return the
        name of the category that best matches the text. """

        # need to escape path separator for the regex matching
        path = string.replace(self.path, os.sep, '\\%s' % os.sep)

        command = CRM_BINARY + (CLASSIFY_CMD % (CLASSIFICATION_TYPE,
                                                self.file_list_string(),
                                                path,
                                                CLASSIFICATION_EXT))
        fin, fout = os.popen2(command)
        #print('- Command:   %s' % command)
        fin.write(text)
        fin.close()

        list = string.split(fout.readline())
        fout.close()

        if list is None:
            return ('', 0.0)
        else:
            category = list[0]
            probability = float(list[1])
            return (category, probability)

    def create_files(self):
        """ Ensures that the associated data files exist by learning an empty
        string. """

        # Create directory if necessary
        if not os.path.exists(self.path):
            os.mkdirs(self.path)

        # Create category files
        for category in self.categories:
            self.learn(category, '')

    def file_list(self):
        """ Returns a list of classification files. """

        # Builds a file path given a category name
        def _file_path(category):
            return os.path.join(self.path, category + CLASSIFICATION_EXT)

        # Return list of all category paths
        return map(_file_path, self.categories)

    # return a list of classification files as a string
    def file_list_string(self):
        """ Returns a list of classification files as a string. """
        return ' '.join(self.file_list())
