import os
import sys
from distutils.sysconfig import get_python_lib

from setuptools import find_packages, setup

# Lookup the version from the code
#version = __import__('cartcurator').__version__
version = '0.1'

EXCLUDE_FROM_PACKAGES = []

install_requires = [line.strip() for line in open("requirements.txt")]

setup(
    name='InputSanitizer',
    version=version,
    url='https://github.com/krishardy/pyinputsanitizer',
    author='Kris Hardy',
    author_email='kris@abqsoft.com',
    description=('Input sanitization library for Python'),
    license='MIT',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    entry_points={},
    extras_require={
    },
    install_requires=install_requires,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
