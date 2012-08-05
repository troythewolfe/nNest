mustache = require 'mustache'
_ = require 'underscore'

viewHelper =
	getView: (build, view) ->
		currView = require build.appRoot + "/views/" + view + "/build.js"
		currView.make build

	setCSS: () ->

	setJS: () ->
	
	getIndex: (build, content) ->
		baseIndexTemplate = require build.baseTemplate
		indexTemplate = require build.index

		baseIndexContent =
			template: mustache.render( indexTemplate, content )

		mustache.render baseIndexTemplate, baseIndexContent

module.exports = viewHelper