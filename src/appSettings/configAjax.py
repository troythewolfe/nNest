from util.configRoot import ConfigRoot
import util.inc as inc

def init(profile):
	#create config object
	config = ConfigRoot()

	#import pages
	import pages.home.config as home
	import pages.calendar.config as calendar
	import pages.todo.config as todo
	config.pages = {
		'home' : home.init(profile),
		'calendar' : calendar.init(profile),
		'todo' : todo.init(profile)	
	}

	#import global views
	import views.nav.config as nav
	config.views = {
		'nav' : nav.init(profile)	
	}

	config.head['title'] = 'here is the default page title'

	return config
