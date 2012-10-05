from util.pageControllerBase import Page

def init(profile):
	page = Page(profile, 'home')
	return page.render('home content')