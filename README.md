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
		'view' : 'pageName'
	}
