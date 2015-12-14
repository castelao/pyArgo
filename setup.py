#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

version = '0.0.3'

requirements = [
        'netCDF4'
]

with open('test-requirements.txt') as test_requirements_file:
    test_requirements = test_requirements_file.read()


setup(
    name='pyARGO',
    version=version,
    description="Python package to handle ARGO profiles.",
    long_description=readme + '\n\n' + history,
    author="Guilherme Castelao",
    author_email='guilherme@castelao.net',
    url='https://github.com/castelao/pyARGO',
    packages=[
        'argo',
        'argo.utils',
    ],
    package_dir={'argo':
                 'argo'},
    include_package_data=True,
    install_requires=requirements,
    license="3-clause BSD",
    zip_safe=False,
    keywords='ARGO oceanography',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
