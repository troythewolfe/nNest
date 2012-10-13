from util.controllerView import View
import os

def init(profile, options={}):
	view = View(profile, 'nav')

	# run-time generated content
	viewContent = {
		'navItems' : 'Some more content!'
	}

	# returns populated view html string
	return view.render(view.get('html')['source'], viewContent)
