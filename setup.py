#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(name='watcherlogger',
      version='1.0',
      description='Cloudwatch Logger Distribution Utilities',
      author='Sreeram',
      author_email='sreeram@accenturefederal.com',
      url='',
      packages=find_packages(include=['watcherlogger', 'watcherlogger.*']),
      package_data={
        'sample': ['package_data.dat'],
      },
      install_requires=[
          'jsonschema','watchtower','requests'
      ],
     )
