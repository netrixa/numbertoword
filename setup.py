import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
  name = 'numbertoword',
  packages = ['numbertoword'],  # this must be the same as the name above
  version = '1.0',
  license=open('LICENSE.txt').read(),
  description = 'Convert number words eg. 1000253 to 1 million, two hundred and fifty three.',
  author = 'Oluwafemi',
  author_email = 'fems.david@hotmail.com',
  url = 'https://github.com/netrixa/numbertoword',  # use the URL to the github repo
  download_url = 'https://github.com/netrixa/numbertoword/archive/master.zip', 
  keywords = ['numbers', 'convert', 'words'],  # arbitrary keywords
  classifiers = [
      'Intended Audience :: Developers',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.6',
  ],
  long_description=open_file('README.rst').read()
)
