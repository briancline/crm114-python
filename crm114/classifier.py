import os;
import string;

#constants

kCrmPath = "crm"

kClassificationType = "<osb unique microgroom>"
kClassificationExtension = ".css"

kLearnCommand = " '-{ learn %s ( %s ) }'"
kClassifyCommand = " '-{ isolate (:stats:); classify %s ( %s ) (:stats:); match [:stats:] (:: :best: :prob:) /Best match to file .. \(%s\/([[:graph:]]+)\\%s\) prob: ([0-9.]+)/; output /:*:best:\\t:*:prob:/ }'"


# wrapper for crm114
class Classifier:

    def __init__( self, path, categories = [] ):
        self.categories = categories
        self.path = path
        self.makeFiles()
        
    # learn the classifier what category some new text is in 
    def learn( self, category, text ):
        command = kCrmPath + ( kLearnCommand % ( kClassificationType, os.path.join( self.path, category + kClassificationExtension ) ) )

        pipe = os.popen( command, 'w' )
        pipe.write( text )
        pipe.close()
    
    # ask the classifier what category best matches some text   
    def classify( self, text ):
        path = string.replace(self.path, os.sep, "\\%s" % os.sep) # need to escape path separator for the regexp matching
        command = kCrmPath + ( kClassifyCommand % (kClassificationType, self.getFileListString(), path, kClassificationExtension) )
        (fin, fout) = os.popen2( command )
        fin.write( text )
        fin.close()
        list = string.split(fout.readline())
        fout.close()
        if list == None:
            return ("", 0.0)
        else:
            category = list[0]
            probability = float(list[1])
            return (category, probability)

    # ensure that data files exist, by calling learn with an empty string
    def makeFiles( self ):
        # make directory if necessary
        if not os.path.exists( self.path ):
                os.mkdir( self.path )

        # make category files
        for category in self.categories:
            self.learn( category, "" )
            
            
    # return a list of classification files
    def getFileList( self ):
        
        # internal method to build a file path given a category
        def getFilePath( file ):
            return os.path.join( self.path, file + kClassificationExtension )
        
        # return list of all category paths
        return map( getFilePath, self.categories )
        

    # return a list of classification files as a string
    def getFileListString( self ):
        return string.join( self.getFileList(), " " )
