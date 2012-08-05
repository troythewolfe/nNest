mustache = require 'mustache'
_ = require 'underscore'
builder = require '../../lib/helpers/builder.js'

make = (build) ->
	headerView = builder.getView build, 'header'

	content =
		header: headerView
		sidebar: 'sidebar'
		content: JSON.stringify build

	builder.getIndex build, content

module.exports.make = make