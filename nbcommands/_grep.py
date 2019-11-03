# -*- coding: utf-8 -*-

import re

from ansimarkup import parse as ansi
import click
import nbformat

from . import __version__


@click.command(name="nbgrep")
@click.version_option(version=__version__)
@click.argument("pattern")
@click.argument("file", nargs=-1)
@click.pass_context
def grep(ctx, *args, **kwargs):
    """Search for a pattern in Jupyter notebooks."""
    pattern = kwargs["pattern"]

    for fin in kwargs["file"]:
        with open(fin, "r") as f:
            nb = nbformat.read(f, as_version=4)

        for cell_n, cell in enumerate(nb.cells):
            for line_n, line in enumerate(cell.source.split("\n")):
                search = re.search(pattern, line)
                if search is not None:
                    first, last = search.span()
                    match = ansi(f"<red>{line[first:last]}</red>")
                    click.echo(
                        ansi("<cyan>:</cyan>").join(
                            [
                                ansi(f"<white>{fin}</white>"),
                                ansi(f"<green>cell {cell_n+1}</green>"),
                                ansi(f"<green>line {line_n+1}</green>"),
                                line.replace(pattern, match),
                            ]
                        )
                    )
