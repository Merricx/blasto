#!/usr/bin/env python
import os
from setuptools import setup

long_description = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()

setup(
	name='blasto',
	version='0.1.0',
	description='A Python implementation of Hill-Climbing for cracking classic ciphers',
	url='https://github.com/merricx/blasto',
	author='Merricx',
	author_email='merricxsherlockian@gmail.com',
	license='Public Domain',
	packages=['modules','modules/cipher','modules/qgr'],
	package_data={'':['modules/keylist']},
	include_package_data=True,
	scripts=['blasto'],
	long_description=long_description,
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Environment :: Console :: Curses",
		"Intended Audience :: Information Technology",
		"Intended Audience :: Science/Research",
		"Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Security :: Cryptography",
        "License :: Public Domain"
	]
)