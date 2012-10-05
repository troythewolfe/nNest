import pages.pageGet as pageGet
from util.pageControllerBase import Page
page = Page()

def init(route):
	return page.render('home')