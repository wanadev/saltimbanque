#!/usr/bin/env python
# encoding: UTF-8

import os.path

from setuptools import setup, find_packages


long_description = ""
if os.path.isfile("README.rst"):
    long_description = open("README.rst", "r").read()


setup(
    name="saltimbanque",
    version="1.0.1",
    description="Provides an API to convert web pages to PDF",

    long_description=long_description,

    author="Wanadev",
    author_email="contact@wanadev.fr",
    maintainer="Fabien LOISON",

    packages=find_packages(),

    install_requires=[
        "Flask",
        "WeasyPrint",
        ],

    entry_points={
        "console_scripts": [
            "saltimbanque = saltimbanque.__main__:main"
        ]
    }

)
