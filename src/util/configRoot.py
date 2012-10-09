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