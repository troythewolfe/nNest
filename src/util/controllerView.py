from util.Get import Get 
get = Get()
import pystache
import os

class View():
	def __init__(self, profile, loc, viewPage=False):
		self.profile = profile
		self.name = loc
		self.viewPage = viewPage
		if not self.viewPage == False:
			self.viewType = 'view'
		else: 
			self.viewType = 'page'
		self.configType = 'view'

	def get(self, ext, fileName=False, options={}):
		return get.get(ext, fileName, options, False, self.name, self.configType, self.viewType)

	def render(self, template, content):
		return pystache.render(template, content)
