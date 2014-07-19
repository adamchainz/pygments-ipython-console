"""Pygments lexer for IPython Console Files
"""

from IPython.sphinxext.ipython_console_highlighting import IPyLexer
#Update IPyLexer to recognise filenames *.ipy
IPyLexer.filenames = ['*.ipy']
