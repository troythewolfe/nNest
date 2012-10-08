import util.inc as inc
import pystache
import os

class View():
	def __init__(self, profile, loc):
		self.profile = profile
		self.name = os.path.split(os.path.dirname(loc))[1]

	def get(self, ext, name=False):
		if name == False:
			name = self.name

		if ext == 'html':
			return inc.html(self.name, 'view', name)

	def render(self, template, content):
		return pystache.render(template, content)