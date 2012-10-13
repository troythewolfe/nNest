from util.Get import Get
import os

class ConfigView(Get):
	def __init__(self, loc, viewPage=False):
		self.name = os.path.split(os.path.dirname(loc))[1]
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
