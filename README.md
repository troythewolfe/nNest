pythonNest
=====

# UNDER CONSTRUCTION

Python, flask and backbone app framework with a focus on putting as much responsibility on the build process as possible and code reuse between device source code.

##CoffeeScript cmd
coffee -o lib/ -cw src/

coffee -cw index.coffee

##TODO
* Adjust all configs to populate from base classes (root, page and view)
* In build process, have a flag to include html templates as js obj
* Bring nested view includes into index
* Make build process adaptable to both index and ajax approaches
* separate out configurable files and utility files (leave configurable files in root, everything else in util)