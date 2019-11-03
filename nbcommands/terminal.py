# -*- coding: utf-8 -*-

from ansimarkup import parse as ansi

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.markup import MarkdownLexer
from pygments.formatters import TerminalTrueColorFormatter


def display(cells):
    output = []

    for cell in cells:
        execution_count = cell.get("execution_count") or " "
        prompt = ansi(f"<green>In [{execution_count}]</green>: ")
        if cell.cell_type == "markdown":
            code = highlight(cell.source, MarkdownLexer(), TerminalTrueColorFormatter())
        else:
            code = highlight(cell.source, PythonLexer(), TerminalTrueColorFormatter())
        output.append(prompt + code)

    return output
