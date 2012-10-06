pythonNest
=====

# UNDER CONSTRUCTION

Python, flask and backbone app framework with a focus on putting as much responsibility on the build process as possible and code reuse between device source code.

##Python Dependencies
* flask
* httpagentparser
* pystache

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
* make build not break when generated directories start out empty
* make framework installable: http://stackoverflow.com/questions/5360873/how-do-i-package-a-python-application-to-make-it-pip-installable
* Adjust all configs to populate from base classes (root, page and view)
* In build process, have a flag to include html templates as js obj
* Add build process watcher to run build.py
* Bring nested view includes into index
* Make build process adaptable to both index and ajax approaches
* separate out configurable files and utility files (leave configurable files in root, everything else in util)