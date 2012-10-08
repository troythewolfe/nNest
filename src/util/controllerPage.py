<<<<<<< HEAD:src/util/controllerPage.py
import util.inc as inc
import pystache

class Page():
  def __init__(self, profile, pageName):
		self.profile = profile
		self.pageName = pageName
  
  def render(self, content):
		self.baseTemplate = inc.index(self.pageName, self.profile['name'])
=======
import util.inc as inc
import pystache

class Page():
  def __init__(self, profile, pageName):
		self.profile = profile
		self.pageName = pageName
  
  def render(self, content):
		self.baseTemplate = inc.index(self.pageName, self.profile['name'])
>>>>>>> f7dc2741760f4abb8096e40ea28c0c9e55643cd2:src/util/controllerPage.py
		return pystache.render(self.baseTemplate['source'], content)