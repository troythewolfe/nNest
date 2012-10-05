import incGet

def init(profile):
	viewName = 'nav'

	return {
		'viewName' : viewName,
		'jsInc' : [
			incGet.js('models/nav', 'view', viewName)
		],
		'cssInc' : [
			incGet.css('nav', 'view', viewName)
		],
	}