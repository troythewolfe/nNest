_ = require 'underscore'

config = (client) ->
	client: client

	#base template defaults
	appDefaults:
		title: 'Welcome to our test site'
		metadata: 
			keywords: 'stuff otherstuff'
			description: 'this is a test site'

	#build definitions

	#TODO: set up so that you only set the filename, then the method that returns it builds out the path and adds the .js
	#TODO: separate it out so that one file into a JSON file and a helper file, leave the JSON in the root
	defineBuilds: () ->
		t = this

		noJS:
			build: __dirname + '/builders/legacyBrowser.js'
			index: __dirname + '/indexes/legacyBrowser.js'
			condition: false
		mobile: 
			build: __dirname + '/builders/mobile.js'
			init: __dirname + '/inits/mobile.js'
			index: __dirname + '/indexes/mobile.js'
			condition: false
		tablet:
			build: __dirname + '/builders/tablet.js'
			init: __dirname + '/inits/mobile.js'
			index: __dirname + '/indexes/tablet.js'
			condition: false
		legacyBrowser:
			build: __dirname + '/builders/legacyBrowser.js'
			init: __dirname + '/inits/legacyBrowser.js'
			index: __dirname + '/indexes/legacyBrowser.js'
			condition: false
		modernBrowser:
			build: __dirname + '/builders/modernBrowser.js'
			init: __dirname + '/inits/modernBrowser.js'
			index: __dirname + '/indexes/modernBrowser.js'
			condition: true #default	


#return config object
module.exports = config