#!/usr/bin/env python

from distutils.core import setup

setup(name='ReadDocs_Test',
      version='1.0',
      author='Jonathan Dorsey',
      packages=['distutils', 'distutils.command', 'numpy', 'torch', 'gym',],
     )