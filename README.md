# nbcommands

[![image](https://img.shields.io/pypi/v/nbcommands.svg)](https://pypi.org/project/nbcommands/) [![image](https://img.shields.io/pypi/pyversions/nbcommands.svg)](https://pypi.org/project/nbcommands/) [![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

nbcommands bring the goodness of Unix commands to Jupyter notebooks.

## Installation

You can simply use pip to install nbcommands:

<pre>
$ pip install nbcommands
</pre>

## Usage

nbcommands gives you the following commands to interact with your Jupyter notebooks without spinning up a notebook server.

- `nbtouch`: Update the access and modification times of each Jupyter notebook to the current time.

    <pre>
    $ nbtouch notebook1.ipynb notebook2.ipynb</pre>
    ![nbtouch](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbtouch.gif)

- `nbgrep`: Search for a pattern in Jupyter notebooks.

    <pre>
    $ nbgrep "os" notebook1.ipynb notebook2.ipynb</pre>
    ![nbgrep](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbgrep.gif)

- `nbhead`: Print the first 5 cells of a Jupyter notebook to standard output.

    <pre>
    $ nbhead notebook1.ipynb</pre>
    ![nbhead](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbhead.gif)

    Note: You can also specify the number of cells you want to print using the `-n` option.
    <pre>
    $ nbhead -n 10 notebook1.ipynb</pre>

- `nbtail`: Print the last 5 cells of a Jupyter notebook to standard output.

    <pre>
    $ nbtail notebook2.ipynb</pre>
    ![nbtail](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbtail.gif)

    Note: You can also specify the number of cells you want to print using the `-n` option.
    <pre>
    $ nbtail -n 10 notebook2.ipynb</pre>

- `nbcat`: Concatenate Jupyter notebooks to standard output.

    <pre>
    $ nbcat notebook1.ipynb notebook2.ipynb</pre>
    ![nbcat](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbcat.gif)

    Note: You can create a new notebook by concatenating multiple notebooks using the `-o` option.
    <pre>
    $ nbcat notebook1.ipynb notebook2.ipynb -o notebook3.ipynb</pre>

- `nbless`: Print a Jupyter notebook using a pager program.

    <pre>
    $ nbless notebook1.ipynb</pre>
    ![nbless](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbless.gif)

And some non-Unix goodness,

- `nbblack`: Blacken Jupyter notebooks.

    <pre>
    $ nbblack notebook1.ipynb notebook2.ipynb</pre>
    ![nbblack](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/docs/_static/nbblack.gif)

Planned enhancements:

- `nbstrip`: Strip outputs from Jupyter notebooks.
- `nbdiff`: Find the diff between two Jupyter notebooks.
- `nbecho`: Add a code cell to a Jupyter notebook.
- `nbedit`: Interactively edit a Jupyter notebook.
- `nbtime`: Run and time a Jupyter notebook.
- `nbwc`: Print word count for a Jupyter notebook.

## Versioning

nbcommands uses [Semantic Versioning](https://semver.org/). For the available versions, see the tags on this repository.

## License

This project is licensed under the Apache License, see the [LICENSE](https://raw.githubusercontent.com/vinayak-mehta/nbcommands/master/LICENSE) file for details.
