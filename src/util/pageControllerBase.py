import pages.pageGet as pageGet
import templates.template as template
import pystache

class Page():
  def __init__(self):
		print 'pageControllerBase init'
  
  def render(self, content):
		self.titleTag = 'a different page title'
		
		#will actually be the 
		self.baseTemplate = 'base'

		templateContent = {
			'title' : self.titleTag,
			'bodyContent' : content
		}
		
		#return 'here is a page'
		return pystache.render(template.get(self.baseTemplate), templateContent)