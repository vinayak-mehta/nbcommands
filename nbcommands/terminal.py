# -*- coding: utf-8 -*-

from colorama import Fore, Style

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalTrueColorFormatter


def display(cells):
    output = []

    for cell in cells:
        try:
            execution_count = cell["execution_count"]
        except KeyError:
            execution_count = " "
        prompt = (
            Fore.GREEN
            + Style.BRIGHT
            + "In [{}]: ".format(execution_count)
            + Style.RESET_ALL
        )
        code = highlight(cell.source, PythonLexer(), TerminalTrueColorFormatter())
        output.append(prompt + code)

    return output
