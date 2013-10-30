#!/usr/bin/python
from os.path import dirname
from crm114 import Classifier


if __name__ == "__main__":
    # perform a simple test
    data_path = dirname(__file__) + '/data'
    c = Classifier( data_path, [ "good", "bad" ] )

    print c.getFileList()
    c.learn( "good", "this is a test" )
    c.learn( "bad", "this is very bad" )
    print "class was: %s, prob was:%f" % ( c.classify( "this is a test" ) )
