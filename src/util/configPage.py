import util.inc as inc
import os

class ConfigPage():
	def __init__(self, loc):
		self.name = os.path.split(os.path.dirname(loc))[1]
		self.html = {}
		self.head = {
			  'title' : self.name
		}
		self.views = {}
		self.jsInc = {}
		self.cssInc = {}

	def get(self, ext, name=False):
		if name == False:
			name = self.name

		if ext == 'html':
			return inc.html(self.name, 'page', name)

		if ext == 'js':
			return inc.js(self.name, 'page', name)