#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='django-permission-tags',
    version='0.1.0',
    author='ted kaemming',
    author_email='ted.kaemming@workshop33.com',
    url='http://github.com/workshop33/django-permission-tags',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
