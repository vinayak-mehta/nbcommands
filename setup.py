# -*- coding: utf-8 -*-

import os
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, "nbcommands", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()


requires = [
    "black>=19.10b0",
    "Click>=7.0",
    "colorama>=0.4.1",
    "nbformat>=4.4.0",
    "Pygments>=2.4.2",
]
dev_requires = ["Sphinx>=2.2.1"]
dev_requires = dev_requires + requires


def setup_package():
    metadata = dict(
        name=about["__title__"],
        version=about["__version__"],
        description=about["__description__"],
        long_description=readme,
        long_description_content_type="text/markdown",
        url=about["__url__"],
        author=about["__author__"],
        author_email=about["__author_email__"],
        license=about["__license__"],
        packages=find_packages(exclude=("tests",)),
        install_requires=requires,
        extras_require={"dev": dev_requires},
        entry_points={
            "console_scripts": [
                "nbblack = nbcommands._black:_black",
                "nbtouch = nbcommands._touch:touch",
                "nbgrep = nbcommands._grep:grep",
                "nbhead = nbcommands._head:head",
                "nbtail = nbcommands._tail:tail",
                "nbcat = nbcommands._cat:cat",
                "nbless = nbcommands._less:less",
            ]
        },
        classifiers=[
            # Trove classifiers
            # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
