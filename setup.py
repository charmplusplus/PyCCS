from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import platform
from os.path import exists
from shutil import copyfile
import distutils
from distutils import log

def get_build_os():
    os = platform.system()
    return os.lower()

system = get_build_os()
libccs_client = None

if system == "darwin":
    try:
        assert os.path.exists('charm_src/charm/lib_so/libccs-client.dylib')
        libccs_client = 'charm_src/charm/lib_so/libccs-client.dylib'
    except AssertionError:
        print("ERROR: Library file 'charm_src/charm/lib_so/libccs-client.dylib' not found!")
        raise
else:
    try:
        assert os.path.exists('charm_src/charm/lib_so/libccs-client.so')
        libccs_client = 'charm_src/charm/lib_so/libccs-client.so'
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
    data_files=[('lib', [libccs_client])]
)
