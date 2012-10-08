from util.controllerPage import Page
import os

def init(profile):
	page = Page(profile, os.path.abspath(__file__))

	pageContent = {
		'title' : 'Calendar Page', 
		'content' : 'here is some home page content'
	}

	if profile['name'] == 'chromeWeb':
		pageContent['title'] = 'Chrome Calendar Page'

	return page.render(pageContent)