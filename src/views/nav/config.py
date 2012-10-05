import inc

def init(profile):
	viewName = 'nav'

	return {
		'viewName' : viewName,
		'jsInc' : [
			inc.js('models/nav', 'view', viewName)
		],
		'cssInc' : [
			inc.css('nav', 'view', viewName)
		],
	}