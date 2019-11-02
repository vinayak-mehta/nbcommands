# -*- coding: utf-8 -*-

import click
import nbformat

from . import __version__
from .terminal import display


@click.command(name="nbless")
@click.version_option(version=__version__)
@click.argument("file")
@click.pass_context
def less(ctx, *args, **kwargs):
    """View the Jupyter notebook to standard output via a Pager"""
    with open(kwargs["file"], "r") as f:
        nb = nbformat.read(f, as_version=4)

    click.echo_via_pager("\n".join(display(nb.cells)))
