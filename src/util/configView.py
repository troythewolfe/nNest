import util.inc as inc
import os

class ConfigView():
	def __init__(self, loc):
		self.name = os.path.split(os.path.dirname(loc))[1]
		self.views = {}
		self.jsInc = {}
		self.cssInc = {}

	def get(self, ext, name=False):
		if name == False:
			name = self.name

		if ext == 'js':
			return inc.js(self.name, 'view', name)