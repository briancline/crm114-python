from os.path import join, dirname
from setuptools import setup


def readme_text(file_name):
    return open(join(dirname(__file__), file_name)).read()


setup(
    name='crm114',
    version='1.0.0a1',
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description=('Python wrapper classes for the CRM-114 Discriminator '
                 '(http://crm114.sourceforge.net/)'),
    license = 'MIT',
    keywords = 'crm114 text analysis classifier',
    url = 'http://packages.python.org/crm-114',
    packages=['crm114', 'tests'],
    long_description=readme_text('README.md'),
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
