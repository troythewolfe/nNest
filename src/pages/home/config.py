import inc

def init(profile):
	pageName = 'home'

	return {
		'pageName' : pageName,
		#'titleTag' : 'This is a better title string',

		'pageTemplate' : inc.html('home', 'page', pageName),

		'jsInc' : [
			inc.js('home', 'page', pageName)
		],
	}