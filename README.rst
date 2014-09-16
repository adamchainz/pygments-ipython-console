========================
pygments-ipython-console
========================
-----------------------------------------
Syntax coloring for IPython Console Files
-----------------------------------------

Overview
========

IPython fails to expose its pygments lexers to pygments. Installing this fixes
that.

Requirements
============
This needs IPython to get at the lexers.

Installation
============

Use your favorite installer to install pygments-ipython into the same Python you have installed Pygments.
Constructing an egg from repository::

	$ git clone https://sanguineturtle@bitbucket.org/sanguineturtle/pygments-ipython-console.git
	$ cd pygments-ipython-console
	$ python setup.py bdist_egg

For example [change directory to dist/ folder to locate egg file]::

	$ easy_install pygments-ipython-console.egg

To verify the installation run::

	$ pygmentize -L lexer | grep -i ipy
	* ipy:
    	IPy session (filenames *.ipy)
