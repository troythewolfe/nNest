import incGet

###############
# Make all configs extend base config class (root, page and view)
###############

def init(profile):
	#import pages
	import pages.home.config as home
	import pages.calendar.config as calendar
	import pages.todo.config as todo

	#import global views
	import views.nav.config as nav

	#profile based config
	pageTitle = 'here is the default page title'

	if profile == 'chromeWeb':
		pageTitle = 'chrome page title' 

	#config object
	return {
		'pages' : {
			'home' : home.init(profile),
			'calendar' : calendar.init(profile),
			'todo' : todo.init(profile)
		},
	
		'views' : {
			'nav' : nav.init(profile)
		},
		
		'titleTag' : pageTitle,
		
		'baseTemplate': 'base',
		
		'jsInc': [
				'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
				incGet.js('third-party/jquery-1.8.2'),
				incGet.js('third-party/backbone-0.9.2'),
				incGet.js('third-party/underscore-1.4.0')
		],
		
		'cssInc' : [
				'http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css',
		  	incGet.css('main')
		]
	}