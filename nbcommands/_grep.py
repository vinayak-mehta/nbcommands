# -*- coding: utf-8 -*-

import re

import click
import nbformat
from colorama import Fore, Style

from . import __version__


def color(s, c, style="bright"):
    color_map = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }
    style_map = {
        "dim": Style.DIM,
        "normal": Style.NORMAL,
        "bright": Style.BRIGHT,
    }

    return color_map[c] + style_map[style] + s + Style.RESET_ALL


@click.command(name="nbgrep")
@click.version_option(version=__version__)
@click.argument("pattern")
@click.argument("file", nargs=-1)
@click.pass_context
def grep(ctx, *args, **kwargs):
    """Search for a pattern in Jupyter notebooks."""
    pattern = kwargs["pattern"]

    for file in kwargs["file"]:
        with open(file, "r") as f:
            nb = nbformat.read(f, as_version=4)

        for cell_n, cell in enumerate(nb.cells):
            for line_n, line in enumerate(cell.source.split("\n")):
                search = re.search(pattern, line)
                if search is not None:
                    first, last = search.span()
                    match = color(line[first:last], "red")
                    click.echo(
                        color(":", "cyan").join(
                            [
                                color(file, "white", style="normal"),
                                color("cell {}".format(cell_n + 1), "green"),
                                color("line {}".format(line_n + 1), "green"),
                                line.replace(pattern, match),
                            ]
                        )
                    )
