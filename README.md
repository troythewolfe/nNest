nNest for python
=====

# UNDER CONSTRUCTION

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
* add cache breaking mechanism to generated files

###Build process
* Add build process watcher to run build.py
* Make build process adaptable to both index and ajax approaches

###Misc
* Document config get template return object
* Make view and page name auto populate, but smarter so they can be nested (pages/ajax/pageName)
* make framework installable: http://stackoverflow.com/questions/5360873/how-do-i-package-a-python-application-to-make-it-pip-installable