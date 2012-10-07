import util.inc as inc
import pystache

class Page():
  def __init__(self, profile, pageName):
		self.profile = profile
		self.pageName = pageName
  
  def render(self, content):
		self.baseTemplate = inc.index(self.pageName, self.profile['name'])
		return pystache.render(self.baseTemplate['source'], content)