from util.controllerPage import Page
<<<<<<< HEAD

print 'page home controller'

=======
>>>>>>> f7dc2741760f4abb8096e40ea28c0c9e55643cd2

def init(profile):
	page = Page(profile, 'home')

	pageContent = {
		'title' : 'Home Page',
		'content' : 'here is some home page content'
	}

	if profile['name'] == 'chromeWeb':
		pageContent['title'] = 'Chrome Home Page'

	return page.render(pageContent)