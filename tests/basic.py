#!/usr/bin/env python
from __future__ import print_function
import os
from operator import itemgetter
from crm114 import Classifier

"""
Performs an extremely basic set of tests by passing some fuzzily-defined words
and phrases to the learner with an explicit sentiment, and runs an equally
fuzzy and arbitrary set of texts through the classifier.

Hopefully it gets them right.
"""


if __name__ == '__main__':
    data_path = '%s%s%s' % (os.path.dirname(__file__), os.sep, 'data')

    categories = ['good', 'bad']

    print('Initializing classifier')
    print('- Categories:  %s' % ', '.join(categories))
    print('- Data path:   %s' % data_path)

    c = Classifier(data_path, ['good', 'bad'])
    for file_path in c.file_list():
        if os.path.exists(file_path):
            os.remove(file_path)

        print('- Data file:   %s' % file_path)

    c.create_files()
    print('')

    c.learn('good', 'this is a good test')
    c.learn('good', 'pretty good')
    c.learn('good', 'this is a VERY good test')
    c.learn('good', 'this is a good test')
    c.learn('good', 'this is a great test')
    c.learn('good', 'awesome test')
    c.learn('good', 'peachy test')
    c.learn('good', 'love')
    c.learn('good', 'hey')
    c.learn('bad', 'a bad test')
    c.learn('bad', 'pretty bad test')
    c.learn('bad', 'this is a very bad test')
    c.learn('bad', 'terrible test')
    c.learn('bad', 'this is a treacherous test')
    c.learn('bad', 'TREACHERY AT ITS FINEST')
    c.learn('bad', 'this is a shit awful test')
    c.learn('bad', 'hate')
    c.learn('bad', 'HATED')  # Case-sensitive? Really?
    c.learn('bad', 'made me care-vomit')
    c.learn('bad', 'vomit')

    classify_texts = ['this is a good test',
                      'here is a pretty good test',
                      'this is a bad test',
                      'this is shit awful',
                      'this is insanely awesome',
                      'THIS IS SUCH AN AWESOME TEST',
                      'I love this test so much.',
                      'This is the finest test.',
                      'HATED IT',
                      "hey baby test, can I get your digits?",
                      'I wanted to vomit',
                      'Please, only the finest of your treachery',
                      'this is a test',
                      'a treacherous, terrible test, which I hated ' +
                      'as it made me vomit']

    category_max = len(max(categories, key=len))
    test_output_format = '%% 3.2f%%%%  %%%ds:  %%s' % category_max

    test_results = []

    for text in classify_texts:
        category, probability = c.classify(text)
        test_results.append({'category': category,
                             'probability': probability,
                             'text': text})

    sorted_results = sorted(test_results, key=itemgetter('probability'),
                            reverse=True)

    for test in sorted_results:
        print(test_output_format % (test['probability'] * 100.0,
                                    test['category'],
                                    test['text']))
