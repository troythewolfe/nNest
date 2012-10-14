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

###Build process
* Dedupe includes by keeping a list of added entries and checking against it on assignment
* Integrate SASS and CoffeeScript

###Build configs
* Add support for page.name.view.name.template paths

###Misc
* Complete wiring for ajax pages, including building ajax templates
* make framework installable: http://stackoverflow.com/questions/5360873/how-do-i-package-a-python-application-to-make-it-pip-installable

####Documenation
* Update all docs
