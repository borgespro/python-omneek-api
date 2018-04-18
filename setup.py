#!/usr/bin/env python
from setuptools import setup, find_packages
import os

from omneek_api import __version__

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = ['requests']

setup(
    name='python-omneek-api',
    version=__version__,
    description='This library is a simple python wrapper for Omneek API',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    url='https://github.com/reisthiago/python-omneek-api.git',
    keywords='omneek',
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires,
    test_suite="omneek_api.tests"
)
