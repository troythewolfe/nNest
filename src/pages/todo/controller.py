<<<<<<< HEAD
from util.controllerPage import Page
page = Page()
=======
from util.controllerPage import View
view = View()
>>>>>>> f7dc2741760f4abb8096e40ea28c0c9e55643cd2

def init(route):
	return view.render('nav content')
