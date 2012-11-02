class ConfigPage():
	def __init__(self, loc):
		self.loc = {}
		self.name = loc
		self.configType = 'page'
		
		self.head = {
			  'title' : self.name
		}
		
		self.views = []
		
		#define asset properties
		self.template = []
		self.js = []
		self.css = []
		self.html = []
		self.lang = []
