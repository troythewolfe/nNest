<<<<<<< HEAD
def init():
	return "run time view html"
=======
from util.controllerView import View
View = View()

def init(route):
	return View.render('calendar')
>>>>>>> added controller and config base objects
