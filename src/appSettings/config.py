import util.inc as inc
from util.configRoot import ConfigRoot

#define global js, css and template includes
def globalInc():
	config = ConfigRoot()

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

	config.templates = [
		inc.template('listItem', 'shared')
	]
	
	return config

def profile(profile):
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

	#html <title>
	pageTitle = 'here is the default page title'

	if profile == 'chromeWeb':
		pageTitle = 'chrome default page title'

	config.head = {
			'title' : pageTitle
	}

	return config