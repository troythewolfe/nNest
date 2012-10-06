import util.inc as inc

def init(profile):
	pageName = 'home'

	return {
		'pageName' : pageName,

		'pageTemplate' : inc.html('home', 'page', pageName),

		'jsInc' : [
			inc.js('home', 'page', pageName)
		],
		
		'jsVersion' : 1,
		
		'cssVersion' : 1
	}
