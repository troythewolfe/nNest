from util.configView import ConfigView
import os

#nav
def init(profile):
	config = ConfigView('nav', 'home')

	'''
	config.css = [
		config.get('css'),
		
		config.get('css', 'nav'),
		
		config.get('css', 'test/nav'),
		
		config.get('css', 'main', {
			'css' : True
		}),
		
		config.get('css', 'nav', {
			'view' : 'nav'
		}),
		
		config.get('css', 'home', {
			'page' : 'home'
		}),
		
		config.get('css', 'nav', {
			'page' : 'home',
			'view' : 'nav'
		})
	]

	config.js = [
		config.get('js'),
		
		config.get('js', 'navSub'),
		
		config.get('js', 'models/nav'),
		
		config.get('js', 'test', {
			'js' : True
		}),
		
		config.get('js', 'nav', {
			'view' : 'nav'
		}),
		
		config.get('js', 'home', {
			'page' : 'home'
		}),
		
		config.get('js', 'navSub', {
			'page' : 'home',
			'view' : 'nav'
		})
	]
	
	#subdirs as part of file name are not allowed, and therefore further directory nesting is not allowed
	config.templates = [
		#call template in local folder with name of view
		config.get('html'),
		
		#call template in local folder with name 'navItem.html'
		config.get('html', 'navItem'),
		
		#get template in 'html/buttons' called 'main.html'
		config.get('html', 'main', {
			'html' : 'buttons',
		}),
		
		#get template in 'views/nav/html' called 'navItem.html'
		config.get('html', 'navItem', {
			'view' : 'nav'
		}),
		
		#get template in 'pages/home/html' called 'navItem.html'
		config.get('html', 'homeSnippet', {
			'page' : 'home'
		}),
		
		#get template in 'pages/home/view/nav/html' called 'navItem.html'
		config.get('html', 'navItem', {
			'page' : 'home',
			'view' : 'nav'
		})
	]
	'''
	
	import views.footer.config as footer
	config.views = {
		'footer' : footer.init(profile)
	}

	return config
