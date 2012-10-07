from util.controllerPage import Page

print 'page home controller'


def init(profile):
	page = Page(profile, 'home')

	pageContent = {
		'title' : 'Home Page',
		'content' : 'here is some home page content'
	}

	if profile['name'] == 'chromeWeb':
		pageContent['title'] = 'Chrome Home Page'

	return page.render(pageContent)