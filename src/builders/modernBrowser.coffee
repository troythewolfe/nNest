mustache = require 'mustache'
_ = require 'underscore'
builder = require '../../lib/helpers/builder.js'

make = (build) ->
	headerView = builder.getView build, 'header'

	content =
		header: headerView
		sidebar: 'sidebar'
		content: '<pre>' + JSON.stringify(build, null, '    ') + '</pre>'

	builder.getIndex build, content

module.exports.make = make