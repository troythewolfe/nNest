from util.controllerPage import Page
import os

def init(profile):
	page = Page(profile, os.path.abspath(__file__))

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

	return page.render(pageContent)