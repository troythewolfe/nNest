from util.pageControllerBase import Page
import config as c
c.init()
page = Page()

def init(route):
	return page.render('calendar')