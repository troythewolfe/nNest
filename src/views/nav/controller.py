from util.controllerView import View
View = View()

def init(route):
	return View.render('calendar')