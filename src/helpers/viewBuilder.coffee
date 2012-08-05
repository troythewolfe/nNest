mustache = require 'mustache'
_ = require 'underscore'

viewHelper =
	getView: (build, view) ->
		currView = require build.appRoot + "/views/" + view + "/build.js"
		currView.make build

module.exports = viewHelper