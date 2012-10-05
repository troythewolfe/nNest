import incGet

def init(profile):
	pageName = 'home'

	return {
		'pageName' : pageName,
		#'titleTag' : 'This is a better title string',

		'pageTemplate' : incGet.html('home', 'page', pageName),

		'jsInc' : [
			incGet.js('home', 'page', pageName)
		],
	}