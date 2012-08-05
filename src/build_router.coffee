mustache = require 'mustache'
_ = require 'underscore'
config = require './config.js'

BASE_TEMPLATE = __dirname + '/indexes/base.js'

setCurrBuild = (client) ->
	conf = config client
	builds = conf.defineBuilds()

	#determine current build based on build condition, 
	#set build params to get passed throughout app construction
	for name, build of builds
		if build.condition
			build.name = name
			build.client = client
			build.baseTemplate = BASE_TEMPLATE
			build.appRoot = __dirname
			build.appDefaults = conf.appDefaults

			delete build.condition
			currBuild = build
			break

	currBuild

getIndex = (client) ->
	currBuild = setCurrBuild client
	builder = require currBuild.build
	builder.make currBuild

module.exports.getIndex = getIndex