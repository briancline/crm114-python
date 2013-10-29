[CRM-114][1] Python Module
==========================

This project is a Python module to interact with [The CRM-114
Discriminator][2], which handles learning and classification of text streams.
While written and used primarily in spam classification, CRM-114 handles text
streams of logs, data, etc. just as well with recorded accuracy rates
exceeding 99.9%. A wide variety of methods can be used with CRM-114, namely
regular expressions, approximate regular expressions, Hidden Markov Model,
Orthogonal Sparse Bigrams (OSB), winnow, general correlation,
K-Nearest-Neighbor, and bit entropy.

Originally crafted by [Sam Deane][3] of [Elegant Chaos][4] and
[Born Sleepy][5], with ongoing improvements and maintenance by
[Brian Cline][6].

This module provides a very simplified interface to CRM-114. It does not
attempt to expose all of CRM-114's power; instead it tries to hide almost all
of the gory details.



Requirements
------------

Python 2.7 is strongly recommended.

Naturally, the `crm` binary itself is required, and should be in your path.
Follow the instructions here for your operating system to install CRM-114.


### Debian, Ubuntu, et al.

    apt-get install crm114

### CentOS, Fedora, Red Hat, et al.

    ## Install and enable the EPEL repository package
    rpm -Uvh http://mirror.steadfast.net/epel/6/i386/epel-release-6-8.noarch.rpm
    yum install --enable-repo=epel crm114

### Everyone else

    ## If you do not yet have libtre and its headers:
    curl -O http://crm114.sourceforge.net/tarballs/tre-0.7.5.tar.gz
    tar -zxf tre-*.tar.gz
    cd tre-*
    ./configure --enable-static
    make
    sudo make install
    cd ..

    curl -O http://crm114.sourceforge.net/tarballs/crm114-20100106-BlameMichelson.src.tar.gz
    tar -zxf crm114-*.tar.gz
    cd crm114*.src
    make
    sudo make install
    cd ..



Installation
------------

This is really all you need:

    sudo pip install crm114



Usage
-----

To use the module, create an instance of the `Classifier` class, giving it the
path to a directory where the data files will be stored, and a list of all
possible category strings--or labels--under which text will be classified.

    c = Classifier("/path/to/my/data", ["good", "bad"])

To teach the classifier object about some text, call the learn method passing
in a category (one of the categories that you previously provided), and the
text.

    c.learn("good", "some good text")
    c.learn("bad", "some bad text")

To find out what the classifier thinks about a body of text, call the classify
method, passing in the text. The result of this method is a pair: the first
item is a category best matching the text, and the second item is the
confidence/probability of that match.

    label, confidence = c.classify("some text")



License
-------

Released under the MIT License. See LICENSE file for details.

Original code licensed under GPLv2, re-licensed 29 October 2013 by Sam Deane
under the MIT license for further curation, maintenance, and packaging.


  [1]: http://en.wikipedia.org/wiki/CRM_114_(fictional_device)
  [2]: http://crm114.sourceforge.net/
  [3]: https://github.com/samdeane
  [4]: http://www.elegantchaos.com/
  [5]: http://bornsleepy.com/
  [6]: https://github.com/briancline
