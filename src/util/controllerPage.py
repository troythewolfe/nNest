import util.inc as inc
import pystache
import os

class Page():
  def __init__(self, profile, loc):
		self.profile = profile
		self.name = os.path.split(os.path.dirname(loc))[1]
  
  def render(self, content):
		if type(content) is dict:
			self.baseTemplate = inc.index(self.name, self.profile['name'])
			return pystache.render(self.baseTemplate['source'], content)
		else:
			return content