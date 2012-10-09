#views

This directory contains web views.  A View is composed of:

	views/
		viewName/
			css/
			html/
			js/
			lang/
			models/
			views/

		config.py
		controller.py

###css, html & js

These folders contain the asset snippets for the view.  The View.get method will, by default, look for a file with name of the view within each of these folders.

For example:
	
	css/viewName.css

###lang

View specific language files

###config.py

Used at build-time.  

`init [Function]`

####Requires

	import util.inc as inc
	from util.configView import ConfigView

####Properties

- `profile [Object]` The profile object as defined in `server.py`

####Returns

- `[ConfigPage]`

####Usage

	def init(profile):
		config = ConfigPage(os.path.abspath(__file__))
	
		# ConfigPage.get looks for an html file
		# with the name of the page
		config.html = config.get('html')
		config.head['title'] = 'home page title set here'
		config.jsInc =[
			config.get('js')
		]
	
		return config

###controller.py

Used at run-time.  

`init [Function]`

####Requires

	from util.controllerPage import Page
	import os

####Properties

- `profile [Object]` The profile object as defined in `server.py`

####Returns

- `[String]` The rendered page content

####Usage

	def init(profile):
		page = Page(profile, os.path.abspath(__file__))
	
		#import views
		import views.nav.controller as nav
	
		#set page content
		pageContent = {
			'title' : 'Home Page',
			'nav' : nav.init(profile),
			'content' : 'here is some home page content'
		}
	
		if profile['name'] == 'chromeWeb':
			pageContent['title'] = 'Chrome Home Page'
	
		return page.render(pageContent)