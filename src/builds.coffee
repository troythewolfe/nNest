mustache = require 'mustache'
_ = require 'underscore'

#define builds
defineBuilds = (device) ->
	noJS:
		build: '../lib/build/legacyBrowser.js'
		index: '../lib/indexes/legacyBrowser.js'
		condition: false
	mobile: 
		build: '../lib/builds/mobile.js'
		init: '../lib/inits/mobile.js'
		index: '../lib/indexes/mobile.js'
		condition: false
	tablet:
		build: '../lib/builds/tablet.js'
		init: '../lib/inits/mobile.js'
		index: '../lib/indexes/tablet.js'
		condition: false
	legacyBrowser:
		build: '../lib/builds/legacyBrowser.js'
		init: '../lib/inits/legacyBrowser.js'
		index: '../lib/indexes/legacyBrowser.js'
		condition: false
	modernBrowser:
		build: '../lib/builds/modernBrowser.js'
		init: '../lib/inits/modernBrowser.js'
		index: '../lib/indexes/modernBrowser.js'
		condition: true

router = (device) ->
	builds = defineBuilds device

	#determine current build based on build condition
	for name, build of builds
		if build.condition
			#add build name and assign to currBuild
			build.name = name
			currBuild = build
			break

	currBuild

route = (device) ->
	route = router device
	build = require route.build
	build.makeIndex route

module.exports.route = route