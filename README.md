#nNest for python

Flask extension for delivering performant, rich and responsive client-side applications.

# UNDER CONSTRUCTION

##Python Dependencies
* flask
* httpagentparser
* pystache
* pyYamlg
* ua-parser (https://github.com/tobie/ua-parser)
* minimatic

##Build:
run src/build.py

##Start Server:
run src/server.py

##CoffeeScript cmd
coffee -o lib/ -cw src/

coffee -cw index.coffee

##Build-time vs Run-time
Config.py files control build time behavior, and Controller.py files control run time.

##TODO
###Cache 
* use filecomp to check if the gen css/js files are different, and if so, add timestamp to break cache ((http://docs.python.org/library/filecmp.html)

###Build process
* Dedupe includes by keeping a list of added entries and checking against it on assignment
* Integrate SASS and CoffeeScript

###Misc
* make framework installable: http://stackoverflow.com/questions/5360873/how-do-i-package-a-python-application-to-make-it-pip-installable
* Add support for root config get shortcuts in Get.py
* Add in logging
* Add in hard fail checks

####Documenation
* Update all docs

####Convert Get.get into json format

	Alternative syntax:

	config.require({
		...
	},{
		...
	},{
		...
	},{
		...
	})

	{
		'type' : 'html' || 'css' || 'js' || 'lang'
		'name' : 'fileName'
		'root' : True || 'htmlFolderName'
		'page' : 'pageName',
		'view' : 'viewName'
	}
	
#### Document these get patterns:

	config.css = [
		config.get('css'),
		
		config.get('css', 'home'),
		
		config.get('css', 'test/home'),
		
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
		
		config.get('js', 'home'),
		
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
		config.get('html', 'homeSnippet'),
		
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
