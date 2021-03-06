from os.path import dirname, join
from setuptools import setup, find_packages, Command 

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

'''
# Implement setupext.janitor which allows for more flexible
# and powerful cleaning. Commands include:

setup.py clean --dist
    Removes directories that the various dist commands produce.
setup.py clean --egg
    Removes .egg and .egg-info directories.
setup.py clean --environment
    Removes the currently active virtual environment as indicated by the $VIRTUAL_ENV environment variable. The name of the directory can also be specified using the --virtualenv-dir command line option.
setup.py clean --pycache
    Recursively removes directories named __pycache__.
setup.py clean --all
    Remove all of by-products. This is the same as using --dist --egg --environment --pycache. 
'''

try:
    from setupext import janitor
    CleanCommand = janitor.CleanCommand
except ImportError:
    CleanCommand = None

cmd_classes = {}
if CleanCommand is not None:
    cmd_classes['clean'] = CleanCommand

with open(join(dirname(__file__), 'README.md'), 'rb' ) as f:
    long_description = f.read().decode('utf-8').strip()

import os
import charactergen
version=charactergen.version

setup (

    name='randomcharacter-generator',
    description='Python package for generating many types of characters',
    url='https://www.github.com/brianthomas/randomcharacter-generator',
    version=version,

    keywords = 'python osr character generator',
    long_description=long_description,

    maintainer='Brian Thomas',
    maintainer_email='galactictaco@gmail.com',

    packages=find_packages(exclude=('tests', 'tests.*')),
    license='MIT License',

    include_package_data=True,

    setup_requires=['setupext-janitor'],
    cmdclass = cmd_classes,

    install_requires=reqs,

)

