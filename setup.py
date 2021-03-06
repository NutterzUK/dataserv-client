#!/usr/bin/env python
# coding: utf-8


import os
from setuptools import setup, find_packages


THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)


VERSION = open("version.txt").readline().strip()
DOWNLOAD_BASEURL = "https://pypi.python.org/packages/source/a/dataserv-client/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "dataserv-client-%s.tar.gz" % VERSION


setup(
    name='dataserv-client',
    version=VERSION,
    description='',
    long_description=open("README.rst").read(),
    keywords=(""),
    url='http://storj.io',
    author='Shawn Wilkinson',
    author_email='shawn+dataserv-client@storj.io',
    license='MIT',
    packages=find_packages(),
    download_url = DOWNLOAD_URL,
    test_suite="tests",
    install_requires=[
        'dataserv == 1.0.1',
    ],
    tests_require=[
        'coverage',
        'coveralls'
    ],
    zip_safe=False,
    classifiers=[
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
