from util.controllerPage import Page

def init(profile):
	page = Page(profile, 'calendar')

	pageContent = {
		'title' : 'Calendar Page', 
		'content' : 'here is some home page content'
	}

	if profile['name'] == 'chromeWeb':
		pageContent['title'] = 'Chrome Calendar Page'

	return page.render(pageContent)