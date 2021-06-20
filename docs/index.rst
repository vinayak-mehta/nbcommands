.. nbcommands documentation master file, created by
   sphinx-quickstart on Sat Aug  1 03:02:35 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

nbcommands — Unix commands for Jupyter notebooks
================================================

.. image:: https://readthedocs.org/projects/nbcommands/badge/?version=latest
    :target: https://nbcommands.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/nbcommands.svg
    :target: https://pypi.org/project/nbcommands/

.. image:: https://img.shields.io/pypi/pyversions/nbcommands.svg
    :target: https://pypi.org/project/nbcommands/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

nbcommands bring the goodness of Unix commands to Jupyter notebooks.

Installation
------------

You can simply use pip to install nbcommands::

    $ pip install nbcommands

or conda::

    $ conda install -c conda-forge nbcommands

Usage
-----

nbcommands installs the following commands which let you interact with your Jupyter notebooks without spinning up a notebook server.

nbtouch
^^^^^^^

Update the access and modification times of each Jupyter notebook to the current time,
or create empty notebook files where none exist::

    $ nbtouch notebook1.ipynb notebook2.ipynb

.. image:: _static/nbtouch.gif

nbgrep
^^^^^^

Search for a pattern in Jupyter notebooks::

    $ nbgrep "os" notebook1.ipynb notebook2.ipynb
    $ nbgrep "os" directory/

.. image:: _static/nbgrep.gif

nbhead
^^^^^^

Print the first 5 cells of a Jupyter notebook to standard output::

    $ nbhead notebook1.ipynb

.. image:: _static/nbhead.gif

.. note:: You can also specify the number of cells you want to print using the ``-n`` option.

nbtail
^^^^^^

Print the last 5 cells of a Jupyter notebook to standard output::

    $ nbtail notebook2.ipynb

.. image:: _static/nbtail.gif

.. note:: You can also specify the number of cells you want to print using the ``-n`` option.

nbcat
^^^^^

Concatenate Jupyter notebooks to standard output::

    $ nbcat notebook1.ipynb notebook2.ipynb

.. image:: _static/nbcat.gif

.. note:: You can create a new notebook by concatenating multiple notebooks using the ``-o`` option.

nbless
^^^^^^

Print a Jupyter notebook using a pager program::

    $ nbless notebook1.ipynb

.. image:: _static/nbless.gif

And some non-Unix goodness,

nbblack
^^^^^^^

Blacken Jupyter notebooks::

    $ nbblack notebook1.ipynb notebook2.ipynb

.. image:: _static/nbblack.gif

---

Planned enhancements:

- ``nbstrip``: Strip outputs from Jupyter notebooks.
- ``nbdiff``: Find the diff between two Jupyter notebooks.
- ``nbecho``: Add a code cell to a Jupyter notebook.
- ``nbedit``: Interactively edit a Jupyter notebook.
- ``nbtime``: Run and time a Jupyter notebook.
- ``nbwc``: Print word count for a Jupyter notebook.

Versioning
----------

nbcommands uses `Semantic Versioning <https://semver.org/>`_. For the available versions, see the tags on the GitHub repository.

License
-------

This project is licensed under the Apache License, see the `LICENSE <https://github.com/vinayak-mehta/nbcommands/blob/master/LICENSE>`_ file for details.
