#!/usr/bin/python

__version__ = "1.0.0a1"

__license__ = """
Copyright (C) 2005 Sam Deane.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
        path = string.replace(self.path, os.pathsep, "\\%s" % os.pathsep) # need to escape path separator for the regexp matching
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

    # perform some self tests   
    def test( self ):
        print self.getFileList()
            self.learn( "good", "this is a test" )
            self.learn( "bad", "this is very bad" )
            print "class was: %s, prob was:%f" % ( self.classify( "this is a test" ) )
        
        
if __name__ == "__main__":
    # perform a simple test
    c = Classifier( "test/data", [ "good", "bad" ] )
    c.test()