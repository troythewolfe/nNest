import inc
import pystache

class Page():
  def __init__(self):
		pass
  
  def render(self, content):
		self.titleTag = 'a different page title'
		
		self.baseTemplate = 'base'

		templateContent = {
			'title' : self.titleTag,
			'bodyContent' : content
		}
		
		return pystache.render(inc.html(self.baseTemplate)['source'], templateContent)