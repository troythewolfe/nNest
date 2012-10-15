from util.Get import Get
get = Get()
import pystache
import os

class Page():
	def __init__(self, profile, loc):
		self.profile = profile
		self.name = loc
		self.configType = 'page'

	def get(self, ext, fileName=False, options={}):
		return get.get(ext, fileName, options, False, self.name, self.configType, False)

	def render(self, content, options):
		if type(content) is dict:
			self.baseTemplate = self.get('index', self.name, self.profile['name'])
			return pystache.render(self.baseTemplate['source'], content)
		else:
			return content
