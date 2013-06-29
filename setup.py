#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""

    tornado-riak

    Copyright (c) 2012-2013 apitrary

"""
from tornadoriak import config

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()
    from setuptools import setup
    from setuptools import find_packages


def read_requirements():
    """
        Read the requirements.txt file
    """
    with open('requirements.txt') as f:
        requirements = f.readlines()
    return [element.strip() for element in requirements]


setup(
    name=config.APP_DETAILS['name'],
    version=config.APP_DETAILS['version'],
    description='Python REST API with Riak library',
    long_description='Tornado-Riak is apitrary\'s base REST API library with Riak support',
    author='Hans-Gunther Schmidt',
    author_email='hgs@apitrary.com',
    maintainer=config.APP_DETAILS['company'],
    maintainer_email=config.APP_DETAILS['support'],
    url='https://github.com/apitrary/tornado-riak',
    packages=find_packages('.'),
    package_dir={'': '.'},
    scripts=[],
    license=config.APP_DETAILS['copyright'],
    install_requires=read_requirements()
)
