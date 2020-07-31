# -*- coding: utf-8 -*-

import click
import nbformat

from . import __version__
from .terminal import display


@click.command(name="nbless")
@click.version_option(version=__version__)
@click.argument("file", type=click.File("rb"), default="-")
@click.pass_context
def less(ctx, *args, **kwargs):
    """View the Jupyter notebook to standard output via a Pager"""

    nb = nbformat.read(kwargs["file"], as_version=4)
    click.echo_via_pager("\n".join(display(nb.cells)))
