from Get import Get
get = Get()

class ConfigPage():
	def __init__(self, loc):
		self.name = loc
		self.configType = 'page'
		self.html = {}
		self.head = {
			  'title' : self.name
		}
		self.views = {}
		self.jsInc = []
		self.cssInc = []
		self.htmlInc = []
		
	def get(self, ext, fileName=False, options={}):
		return get.get(ext, fileName, options, False, self.name, self.configType, False)
