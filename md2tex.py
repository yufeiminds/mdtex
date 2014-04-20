#coding=utf8

"""
File: md2tex.py
Author: Li-Yufei
Create: 2014-04-17 20:43:37 by Li-Yufei

License:
	MIT: http://en.wikipedia.org/wiki/MIT_License

Discription:
	This is a file to parse MarkDown text to LaTex text
	The model is only to study, please don't use it in your project
"""

import re

rhead = re.compile('(?:\n)(#+)\s+([^\n]*)')
rquote = re.compile('(?:\n)>\s+([^(?:\n\n)]*)')
rverbatim = re.compile('((\n[\t| {4}][^(?:\n\n)]+)+)')
rit = re.compile('\*([^*\n]*)\*')
rabstract = re.compile('\[\[\s*([^]]*)\s*\]\]')

rtitle = re.compile('\n#\s+([^\n]*)')

class md2tex():
	def __init__(self):
		self.text = ''
		self.hdict = {
				'#':		'\chapter',
				'##':		'\section',
				'###':	'\subsection',
				'####':	'\subsubsection'
			}
		self.escapes_dict = {
				'\\': '\\textbackslash',
				'~': '\\textasciitilde',
				'$': '\\textdollar',
				'_': '\\textunderscore',
				'^': '\\textasciicircum',
				'{': '\\textbraceleft',
				'}': '\\textbraceright',
				'<': '\\textless',
				'>': '\\textgreater',
				'|': '\\textbar'
		}

		self.unescapes_dict = {
				'\\textbackslash': '\\',
				'\\textasciitilde': '~',
				'\\textdollar': '$',
				'\\textunderscore': '_',
				'\\textasciicircum': '^',
				'\\textbraceleft': '{',
				'\\textbraceright': '}',
				'\\textless': '<',
				'\\textgreater': '>',
				'\\textbar': '|'
		}

	def loadmd(self, path):
		self.text = open(path, "r").read()

	def parse(self):
		self.escapes()
		# Match title
		self.text = rhead.sub(lambda m: '\n' + self.hdict[m.group(1)] + '{' + m.group(2) + '}\n', self.text)

		# Match quote
		self.text = rquote.sub(lambda m: '\n\\begin{quote}\n' + m.group(1) + '\n\\end{quote}\n', self.text)

		# Match text/code block
		self.text = rverbatim.sub(lambda m: self.unescapes('\n\\begin{verbatim}' + m.group(1) + '\n\\end{verbatim}\n'), self.text)

		# Match star tag (means italic font)
		self.text = rit.sub(lambda m: '\\textit{ %s }' % m.group(1), self.text)

		# Match abstract
		self.text = rabstract.sub(lambda m: '\n\\begin{abstract}\n %s \\end{abstract}\n' % m.group(1), self.text)

		return self.text

	# process escapes character
	def escapes(self):
		self.text = self.text.replace('\\', '\\textbackslash')
		self.text = self.text.replace('~', '\\textasciitilde')
		self.text = self.text.replace('$', '\\textdollar')
		self.text = self.text.replace('_', '\\textunderscore')
		self.text = self.text.replace('^', '\\textasciicircum')
		self.text = self.text.replace('{', '\\textbraceleft')
		self.text = self.text.replace('}', '\\textbraceright')
		self.text = self.text.replace('<', '\\textless')
		self.text = re.sub(r'[^\n]>', '\\textgreater', self.text)
		self.text = self.text.replace('|', '\\textbar')

	# process unescapes character
	def unescapes(self, s):
		for keys in self.unescapes_dict:
			s = s.replace(keys, self.unescapes_dict[keys])
		return str(s)

	# return the title of markdown document
	def getTitle(self):
		return rtitle.search(self.text).group(1)
