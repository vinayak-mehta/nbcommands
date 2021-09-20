# -*- coding: utf-8 -*-

from colorama import Fore, Style

from pygments import highlight
from pygments.lexers import MarkdownLexer, PythonLexer, TextLexer
from pygments.formatters import TerminalTrueColorFormatter


def display(cells):
    output = []

    for cell in cells:
        prompt = ""
        
        # TODO: show more cell types
        if cell["cell_type"] == "code":
            execution_count = cell.get("execution_count")
            execution_count = execution_count and execution_count or " "
            prompt = (
                Fore.GREEN
                + Style.BRIGHT
                + "In [{}]: ".format(execution_count)
                + Style.RESET_ALL
            )
            lexer = PythonLexer()    
            
        elif cell["cell_type"] == "markdown":
            lexer = MarkdownLexer()
           
        else:
            lexer = TextLexer()
            
        code = highlight(cell.source, lexer, TerminalTrueColorFormatter())
        output.append(prompt + code)

    return output
