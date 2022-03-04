from setuptools import setup, find_packages

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
    ]
)
