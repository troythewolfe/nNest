class ConfigPage():
  def __init__(self, name):
		self.name = name
		self.template = ''
		self.views = {}
		self.jsInc = {}
		self.cssInc = {}

	def set(self, key, name):
		if key == 'template':
			if !name:
				name = self.name
			return inc.html(self.name, 'page', name)