import util.inc as inc
from util.configRoot import ConfigRoot

def init(profile):
	#create config object
	config = ConfigRoot()

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
	config.pages = {
		'home' : home.init(profile),
		'calendar' : calendar.init(profile),
		'todo' : todo.init(profile)	
	}

	config.views = {
		'nav' : nav.init(profile)	
	}

	config.head = {
			'title' : pageTitle
	}

	config.baseTemplate = 'base'

	config.jsInc = [
		'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
		inc.js('third-party/jquery-1.8.2'),
		inc.js('third-party/underscore-1.4.0'),
		inc.js('third-party/backbone-0.9.2')
	]

	config.cssInc = [
		'http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css',
		inc.css('main')
	]

	return config
