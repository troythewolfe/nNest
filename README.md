nNest
=====

Node and backbone js server/client framework with a focus on code reuse between device builds

##Required modules
* express
* mustache
* ua-parser
* underscore

##CoffeeScript cmd
TODO: Grunt these tasks
coffee -o lib/ -cw src/
coffee -cw index.coffee

##Framework Components

###index.js
* starts express server
* sets up static 'public' folder
* sets up base path listeners
* calls buildRouter and passes client (parsed user-agent) data
* sends the built index to the client

###build_router.js
The first build object that has a 'true' condition is set the current build.  This build will determine which index.html, build controller and client init file will be used to construct this app.  The build name is passed down during the build process, so individual views can construct themselves differently depending on the current build name (or specific params within the build object)
* sets the current build object based on conditions within config.js

###config.js
* sets up build objects
 * build (path to specific build file for this build)
 * index (path to index template to use for this build)
 * init (path to init js file that will be sent to client for this build)
 * condition (the conditions that have to be met to use this build, generally based on the helpers/client.js object
* sets base template properties
* sets global js and css (if any)

###helpers/client.js
* user-agent parsing
* returns formatted client object


###builders/builder_name.js
* an index builder that is assigned to one or more builds
* retrieves views
* retrieves and pushes css and js includes
* constructs and returns index
