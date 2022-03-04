from setuptools import setup, find_packages
from setuptools.command.install import install
import os
from os.path import exists
from shutil import copyfile
import distutils
from distutils import log

try:
    assert os.path.exists('charm_src/charm/lib_so/libccs-client.so')
except AssertionError:
    print("ERROR: Library file 'charm_src/charm/lib_so/libccs-client.so' not found!")
    raise

setup(
    name="PyCCS",
    version="0.01",
    packages = ['pyccs'],
    install_requires = [""],
    extras_require={'tests': ['pytest']},
    author = "Zane Fink",
    author_email = "zanef2@illinois.edu",
    description = "Python CCS Interface",
    long_description = "",
    license = "",
    keywords = "pytest testing",
    url = "",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    data_files=[('lib', ['charm_src/charm/lib_so/libccs-client.so'])]
)
