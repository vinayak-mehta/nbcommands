# -*- coding: utf-8 -*-

from ansimarkup import parse as ansi

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.markup import MarkdownLexer
from pygments.formatters import TerminalTrueColorFormatter

LEXER_MAP = {"markdown": MarkdownLexer(), "code": PythonLexer()}


def display(cells):
    output = []

    for cell in cells:
        execution_count = cell.get("execution_count") or " "
        prompt = ansi(f"<green>In [{execution_count}]</green>: ")
        code = highlight(
            cell.source, LEXER_MAP[cell.cell_type], TerminalTrueColorFormatter()
        )
        output.append(prompt + code)

    return output
