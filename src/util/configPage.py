from util.Get import Get
import os

class ConfigPage(Get):
	def __init__(self, loc):
		self.name = os.path.split(os.path.dirname(loc))[1]
		self.configType = 'page'
		self.html = {}
		self.head = {
			  'title' : self.name
		}
		self.views = {}
		self.jsInc = []
		self.cssInc = []
		self.htmlInc = []
