<<<<<<< HEAD
from util.controllerPage import Page
=======
<<<<<<< HEAD
from util.pageController import Page
=======
from util.controllerPage import Page
>>>>>>> added controller and config base objects
>>>>>>> f7dc2741760f4abb8096e40ea28c0c9e55643cd2
page = Page()

def init(route):
	return page.render('calendar')
