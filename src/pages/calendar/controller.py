<<<<<<< HEAD
from util.pageController import Page
=======
from util.controllerPage import Page
>>>>>>> added controller and config base objects
page = Page()

def init(route):
	return page.render('calendar')
