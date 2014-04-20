[[
this block is abstract
]]

# README

## About the package
Thank for your reading.
I'm a student and this package is create on my lesson for python/latex.
I'm sorry to there are some bug have no fixed and more bug in unknown runtime.
I hope use MVC(Model-View-Control) design patterns into LaTeX Writing(sure, there is no model part).
This page is compiled with pyLatex(call the latex:pdflatex commands) if you are reading README.pdf, it also can find from output directory.

### Directory structure

	├── pyTex
	│   ├── demo.py
	│   ├── __init__.py
	│   ├── md2tex.py
	│   ├── output
	│   ├── pyLatex.py
	│   └── templates
	│       └── example.tex
	└── setup.py

#### Subdirectories
We have two special default directories *output* and *templates*, and the directories also can be changed in pyLatex.py. you can create and modify your own LaTeX templates in your templates directory, and call compile method to output tex/pdf file in your output directory.

#### Source Code
There are two python class, pyLatex class to parse templates tags and render content from user to templates, it also have a method named compile that call the command *pdflatex* from LaTeX software.
So you need to install LaTeX, if you on ubuntu(linux with apt-get) platform, can use:
> sudo apt-get install texlive-latex-*

if you need multi-lang, for example cjk:

> sudo apt-get install latex-cjk-all

and use it in your templates.

We have a demo in *demo.py*, if you had installed LaTeX, can use it to compile this README demo.

## Basic syntax in markdown

> Small memo with MarkDown, Big paper with LaTeX.

I am sorry to that the package only can use the following syntax
and also can't insert newline symbol(except in block content)
It only a model for easy to use, sure you can use LaTeX syntax by pyLatex, it's beautiful but not conciser than markdown.

### title
	like this title, with 1~4 '#' to mark it

### block
	text/code block
	this is block area

### quote
> hello, -- LaTeX  World -- !

### italic
a line with *italic* font

## Contact Me
If you have question, suggestion or want to make it better together, please send mail to me:

>	sanguo0023@gmail.com

Thanks Again!
