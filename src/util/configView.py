class ConfigView():
	def __init__(self, loc, viewPage=False):
		self.loc = {}
		self.name = loc
		self.viewPage = viewPage
		
		#assign viewType
		if not self.viewPage == False:
			self.viewType = 'view'
		else: 
			self.viewType = 'page'
			
		self.configType = 'view'
		
		#define asset properties
		self.views = []
		self.js = []
		self.css = []
		self.html = []
		self.lang = []
