from util.controllerPage import Page
page = Page()

def init(route):
	return page.render('calendar')