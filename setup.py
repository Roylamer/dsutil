from distutils.core import setup
setup(
  name = 'dsutil',
  packages = ['dsutil'], # this must be the same as the name above
  version = '0.0.1',
  description = 'Package sharable code',
  author = 'Icarus So',
  author_email = 'icarus.so@tvb.com',
  url = '', # use the URL to the github repo
  keywords = [], # arbitrary keywords
  classifiers = [],
  install_requires=[
    'nbparameterise'
  ]
)