nNest for python
=====

# UNDER CONSTRUCTION

*Currently in a broken state*

Python, flask and backbone app framework with a focus on putting as much responsibility on the build process as possible and code reuse between device source code.

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
* if the file contents are different, then update timestamp

###Build process
* Dedupe includes by keeping a list of added entries and checking against it on assignment
* Install and integrate scss into build process (SASS CSS compiler) http://packages.python.org/scss/
* Determine good conditional to import build.py into server.py
* Make build process adaptable to both index and ajax approaches
* Pages can be made ajax style by declaring a different base template

###Build configs
* Add support for page.name.view.name.template paths

###Misc
* Ajax view by routing to a view controller (will return rendered view html)
* Document patterns for wiring ajax pages, such as calling a regular config from within an ajax page config, then adding anything necessary
* Add support for inc within a page.view
* Document config get template return object
* Make view and page name auto populate, but smarter so they can be nested (pages/ajax/pageName)
* make framework installable: http://stackoverflow.com/questions/5360873/how-do-i-package-a-python-application-to-make-it-pip-installable
