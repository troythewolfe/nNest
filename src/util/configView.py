import util.inc as inc           
import os

class ConfigView():
	def __init__(self, loc):
		self.name = os.path.split(os.path.dirname(loc))[1]
		self.views = {}
		self.jsInc = []
		self.cssInc = []
		self.htmlInc = []

	def get(self, ext, name=False, loc=False):
		if name == False:
			name = self.name

		if ext == 'html':
			return inc.html(name, 'view', self.name)

		if ext == 'css':
			return inc.css(name, 'view', self.name)

		if ext == 'js':
			return inc.js(name, 'view', self.name)

		if ext == 'template':
			if loc == False:
				htmlItem = inc.html(name, 'view', self.name)
				htmlItem['name'] = name
				htmlItem['type'] = 'view'
				htmlItem['typeName'] = self.name
				return htmlItem
			else:
				htmlName = loc + '/' + name
				htmlItem = inc.html(htmlName)
				htmlItem['name'] = name
				htmlItem['type'] = 'html'
				htmlItem['typeName'] = loc
				return htmlItem