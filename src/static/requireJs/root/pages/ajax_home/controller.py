from util.controllerPage import Page
import os

def init(profile, options={}):
	page = Page(profile, 'home')

	'''
	#import views
	import views.nav.controller as nav

	#set page content
	pageContent = {
		'title' : 'Home Page',
		'nav' : nav.init(profile),
		'content' : 'here is some home page content'
	}
	
	if profile['name'] == 'chromeWeb':
		pageContent['title'] = 'Chrome Home Page'
	'''
	
	pageContent = {
		'title' : 'Home Page'
	}
	
	return page.render(pageContent, options)
