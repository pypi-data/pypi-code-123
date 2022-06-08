#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-module-docstring,exec-used

import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

# DO NOT EDIT THIS NUMBER!
# IT IS AUTOMATICALLY CHANGED BY python-semantic-release
__version__ = "1.13.3"

setuptools.setup(
    name='molcas_suite',
    version=__version__,
    author='Chilton Group',
    author_email='nicholas.chilton@manchester.ac.uk',
    description='A package for dealing with OpenMOLCAS input and output files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.com/chilton-group/molcas_suite",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
        ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'scipy',
        'h5py',
        'xyz_py>=4.2.0',
        'angmom_suite>=1.7.5',
        'hpc_suite>=1.3.0',
        'matplotlib'
        ],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'molcas_suite = molcas_suite.cli:main'
            ]
        }
    )
