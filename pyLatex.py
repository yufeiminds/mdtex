#coding=utf8

"""
File: pyLatex.py
Author: Li-Yufei
Create: 2014-04-17 20:43:37 by Li-Yufei

License:
	MIT: http://en.wikipedia.org/wiki/MIT_License

Discription:

"""


import re
from commands import getstatusoutput
re_exp = re.compile('({%\s*?(\w+)\s*?%})')
re_exp_title = re.compile('\\\\title{\s*([^}]+?)\s*}')


class pyLatex():
	def __init__(self):
		self.doctype = 'report'
		self.template = './templates/'
		self.output = './output/'
		self.title = 'Default'
		self.template_file = None
		self.template_text = None

	def render(self, fname = 'default.tex', params = {}):
		if fname is not None and type(params) is dict:
			# Open template file
			try:
				self.template_file = open(self.template + fname, "r")
			except:
				print "Failed to open tex template file"

			self.template_text = self.template_file.read()

			# Replace template tag
			for item in re_exp.findall(self.template_text):
				if item[1] in params.keys():
					self.template_text = self.template_text.replace(item[0], params[item[1]])
			
			# Parse the title of LaTex document
			try:
				self.title = (re_exp_title.search(self.template_text).groups())[0]
			except:
				print "Uneable template, please check your \\title."

			# Render to the latex template
			try:
				tmp = open(self.output + unicode(self.title, "utf8") + '.tex', "w")
				tmp.write(self.template_text)
				tmp.close()
			except:
				print "Error to write!"
			
			print self.title + " is success for render to template."

			return 0

	# Use "pdflatex" command to compile latex document
	# If you want to make title, please call it twice
	def compile(self):
		cmd = 'pdflatex -output-directory ' + self.output + " " + self.output + self.title + '.tex'

		status, output = getstatusoutput(cmd)
		if status is 0:
			print "compile successfully."
		else:
			print output

	def chapter(self, title=None):
		if title is not None:
			rtext = '\n\\chapter{ ' + title + ' }\n'
			return rtext
		else:
			return ''

	def section(self, title=None):
		if title is not None:
			rtext = '\n\\section{ ' + title + ' }\n'
			return rtext
		else:
			return ''

	def quote(self, text=''):
		rtext = '\n\\begin{quote}\n' + text + '\n\\end{quote}\n'
		return rtext

	def verbatim(self, text=''):
		rtxt = '\n\\begin{verbatim}\n' + text + '\n\\end{verbatim}\n'
		return rtext
