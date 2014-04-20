#coding=utf8

"""
File: exec.py
Author: Li-Yufei
Create: 2014-04-17 20:43:37 by Li-Yufei

License:
	MIT: http://en.wikipedia.org/wiki/MIT_License

Discription:

"""

import md2tex
import pyLatex

md = md2tex.md2tex()
latex = pyLatex.pyLatex()

md.loadmd("./README.md")

# Get params that you have defined in templates.
params = {'title': md.getTitle(), 'content': md.parse()}

# Render params to templates
latex.render('example.tex', params)

# Compile twice, first for content, second for index.
latex.compile()
latex.compile()
