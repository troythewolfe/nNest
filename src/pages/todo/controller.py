from util.controllerPage import View
view = View()

def init(route):
	return view.render('nav content')