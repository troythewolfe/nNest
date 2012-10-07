class ConfigRoot():
  def __init__(self):
		self.pages = {}
		self.views = {}
		self.head = {
			'title' : ''
		}
		self.baseTemplate = ''
		self.jsInc = {}
		self.cssInc = {}
		