# -*- coding: utf-8 -*-

import pathlib
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
@click.argument("file", nargs=-1, type=click.Path(exists=True), required=True)
@click.pass_context
def grep(ctx, *args, **kwargs):
    """Search for a pattern in Jupyter notebooks."""
    pattern = kwargs["pattern"]
    
    def collect_files():
        """generator for paths
        
        FILE can be individual files or directories.
        If it's a directory, find all .ipynb files in the directory.
        """
        for path in kwargs["file"]:
            path = pathlib.Path(path)
            if path.is_dir():
                for filename in path.glob("**/*.ipynb"):
                    yield filename
            else:
                yield path

    for file in collect_files():
        filename = str(file)
        with file.open("r") as f:
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
                                color(filename, "white", style="normal"),
                                color("cell {}".format(cell_n + 1), "green"),
                                color("line {}".format(line_n + 1), "green"),
                                line.replace(pattern, match),
                            ]
                        )
                    )
