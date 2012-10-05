import inc
import pystache
import sys
sys.path.append('/')

indexPath = 'indexes/'

class Page():
  def __init__(self, profile, pageName):
		self.profile = profile
		self.pageName = pageName
  
  def render(self, content):
		self.titleTag = 'a different page title'

		self.baseTemplate = inc.index(self.pageName, self.profile['name'])

		templateContent = {
			'title' : self.titleTag,
			'bodyContent' : content
		}
		
		return pystache.render(self.baseTemplate['source'], templateContent)