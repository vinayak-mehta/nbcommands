# -*- coding: utf-8 -*-

import os
from pathlib import Path

import click
import nbformat

from . import __version__


@click.command(name="nbtouch")
@click.version_option(version=__version__)
@click.argument("file", nargs=-1)
@click.pass_context
def touch(ctx, *args, **kwargs):
    """Update the access and modification times of each Jupyter notebook to the current time.

    If FILE does not exist, it will be created as an empty notebook.
    """
    for file in kwargs["file"]:
        if not os.path.exists(file):
            nb = nbformat.v4.new_notebook()
            with open(file, "w") as f:
                nbformat.write(nb, f, version=4)
        else:
            Path(file).touch()
