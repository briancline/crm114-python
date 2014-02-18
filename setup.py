from setuptools import setup

VERSION = '2.0.2'
VERSION_TAG = 'v%s' % VERSION
README_URL = ('https://github.com/briancline/crm114-python'
              '/blob/%s/README.md' % VERSION_TAG)

setup(
    name='crm114',
    version=VERSION,
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description=('Python wrapper classes for the CRM-114 Discriminator '
                 '(http://crm114.sourceforge.net/)'),
    license = 'MIT',
    keywords = 'crm114 text analysis classifier kubrick',
    url = 'http://packages.python.org/crm114',
    packages=['crm114'],
    long_description='See README.md for full details, or %s.' % README_URL,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Adaptive Technologies',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
)
