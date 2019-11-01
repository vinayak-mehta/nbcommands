# -*- coding: utf-8 -*-

import click
import nbformat

from . import __version__
from .terminal import display


@click.command(name="nbhead")
@click.version_option(version=__version__)
@click.option(
    "-n",
    "--lines",
    default=5,
    help="Print the first INTEGER lines instead of the first 5.",
)
@click.argument("file")
@click.pass_context
def head(ctx, *args, **kwargs):
    """Print the first 5 cells of a Jupyter notebook to standard output."""
    with open(kwargs["file"], "r") as f:
        nb = nbformat.read(f, as_version=4)

    n = kwargs["lines"]
    cells = nb.cells[:n]
    click.echo("\n".join(display(cells)))
