# -*- coding: utf-8 -*-

import os

import click
import nbformat

from . import __version__
from .terminal import display


@click.command(name="nbcat")
@click.version_option(version=__version__)
@click.option("-o", "--output", help="Output file path.")
@click.argument("file", nargs=-1)
@click.pass_context
def cat(ctx, *args, **kwargs):
    """Concatenate Jupyter notebooks to standard output."""
    # Source: https://github.com/jbn/nbmerge
    merged, metadata = None, []

    for file in kwargs["file"]:
        with open(file, "r") as f:
            nb = nbformat.read(f, as_version=4)

        metadata.append(nb.metadata)

        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)

    merged_metadata = {}
    for meta in reversed(metadata):
        merged_metadata.update(meta)
    merged.metadata = merged_metadata

    if kwargs["output"] is not None:
        with open(kwargs["output"], "w") as f:
            nbformat.write(merged, f, version=4)
    else:
        click.echo("\n".join(display(merged.cells)))
