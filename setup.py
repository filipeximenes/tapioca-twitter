#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
import os
import sys


package = 'tapioca_twitter'
readme = open('README.rst').read()
requirements = [
    'tapioca-wrapper',
    'requests_oauthlib',
]
test_requirements = [

]

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

setup(
    name='tapioca-twitter',
    version=get_version(package),
    description='Twitter API wrapper using tapioca',
    long_description=readme,
    author='Filipe Ximenes',
    author_email='filipeximenes@gmail.com',
    url='https://github.com/filipeximenes/tapioca-twitter',
    packages=[
        'tapioca-twitter',
    ],
    package_dir={'tapioca-twitter':
                 'tapioca_twitter'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='tapioca_twitter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
