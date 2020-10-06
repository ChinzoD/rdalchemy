#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='rdalchemy',
      version='0.0.21',
      description='Using SQLAlchemy with chemical databases',
      packages=['rdalchemy'],
      install_requires=[
          'psycopg2-binary',
          'SQLAlchemy>=0.7.0',
      ],
)
