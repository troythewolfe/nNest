import util.inc as inc
import pystache

class View():
  def __init__(self, profile, viewName):
		self.profile = profile
		self.viewName = viewName
  
  def render(self, content):
		#self.baseTemplate = inc.index(self.pageName, self.profile['name'])
		
		#return pystache.render(self.baseTemplate['source'], content)
		return content