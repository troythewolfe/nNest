from util.controllerView import View
import os

def init(profile):
	view = View(profile, os.path.abspath(__file__))

	# run-time generated content
	viewContent = {
		'navItems' : 'Some more content!'
	}

	# returns populated view html string
	return view.render(view.get('html')['source'], viewContent)