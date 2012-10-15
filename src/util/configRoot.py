from util.Get import Get
get = Get()

class ConfigRoot():
	def __init__(self):
		self.pages = {}
		self.views = {}
		self.head = {
			'title' : ''
		}
		self.baseTemplate = 'base'
		self.jsInc = []
		self.cssInc = []
		self.templates = []
					
	def get(self, ext, fileName=False, options={}):
		return get.get(ext, fileName, options, False, False, False, False)
