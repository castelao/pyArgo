#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
        'pupynere'
]

setup(
    name='pyargo',
    version='0.0.1',
    description="Python package to handle ARGO profiles.",
    long_description=readme + '\n\n' + history,
    author="Guilherme Castelao",
    author_email='guilherme@castelao.net',
    url='https://github.com/castelao/argo',
    packages=[
        'argo',
    ],
    package_dir={'argo':
                 'argo'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='argo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
    ],
)
