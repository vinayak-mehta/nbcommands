# -*- coding: utf-8 -*-

import re

import black
import click
import nbformat

from . import __version__


def _cells(nb):
    """Yield all cells in an nbformat-insensitive manner

    Source: https://github.com/kynan/nbstripout/blob/master/nbstripout/_utils.py#L27
    """
    if nb.nbformat < 4:
        for ws in nb.worksheets:
            for cell in ws.cells:
                yield cell
    else:
        for cell in nb.cells:
            yield cell


@click.command(name="nbblack")
@click.version_option(version=__version__)
@click.argument("file", nargs=-1)
@click.pass_context
def _black(ctx, *args, **kwargs):
    """Blacken Jupyter notebooks."""
    file_count = len(kwargs["file"])
    black_file_count = 0

    for file in kwargs["file"]:
        with open(file, "r") as f:
            nb = nbformat.read(f, as_version=4)

        black_flag = False
        pinfo_flag = False
        pattern = re.compile("^\?")
        # Source: https://neuralcoder.science/Black-Jupyter/
        for cell in _cells(nb):
            if cell.cell_type == "code":
                source = cell.source
                source = re.sub("^%", "#%", source, flags=re.M)
                source = re.sub("^!", "#!", source, flags=re.M)
                if pattern.match(source):
                    pinfo_flag = True
                    source = "#" + source
                black_source = black.format_str(source, mode=black.FileMode())
                black_source = re.sub("^#%", "%", black_source, flags=re.M)
                black_source = re.sub("^#!", "!", black_source, flags=re.M)
                if pinfo_flag:
                    black_source = black_source[1:]
                black_source = black_source.strip()
                if cell.source != black_source:
                    black_flag = True
                cell.source = black_source

        if black_flag:
            click.echo("reformatted {}".format(file))
            black_file_count += 1

        with open(file, "w") as f:
            nbformat.write(nb, f, version=4)

    click.echo("All done! ✨ 🍰 ✨")
    if black_file_count:
        s = "s" if black_file_count > 1 else ""
        click.echo("{} file{} reformatted.".format(black_file_count, s))
    else:
        s = "s" if file_count > 1 else ""
        click.echo("{} file{} left unchanged.".format(file_count, s))
