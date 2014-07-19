"""Pygments lexer for IPython Console Files
"""

from IPython.sphinxext.ipython_console_highlighting import IPyLexer
#Update IPythonConsole Lexer to recognise filenames *.ipy
IPyLexer.filenames = ['*.ipy']
