from util.Get import Get 
get = Get()
import os

class ConfigView():
	def __init__(self, loc, viewPage=False):
		self.name = loc
		self.viewPage = viewPage
		if not self.viewPage == False:
			self.viewType = 'view'
		else: 
			self.viewType = 'page'
		self.configType = 'view'
		
		self.views = {}
		self.jsInc = []
		self.cssInc = []
		self.htmlInc = []

	def get(self, ext, fileName=False, options={}):
		#return self.name
		return get.get(ext, fileName, options, self.viewPage, self.name, self.configType, self.viewType)
