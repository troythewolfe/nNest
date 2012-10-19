from util.controllerPage import Page
import os

def init(profile):
	page = Page(profile, os.path.abspath(__file__))

	pageContent = {
		'title' : 'Home Page',
		'content' : 'here is some home page content'
	}

	if profile['name'] == 'chromeWeb':
		pageContent['title'] = 'Chrome Home Page'

	return page.render(pageContent)