uaParser = require 'ua-parser'

#based on http://stackoverflow.com/questions/6163350/server-side-browser-detection-node-js
detect = (request) ->
	ua = request.headers['user-agent']
	device =
		userAgent: ua
		browser: uaParser.parse ua
		path: request.url
		type: {}

	if /mobile/i.test ua 
	then device.type.mobile = true 

	if /Windows NT/.test ua 
	then device.type.windows =  /Windows NT ([0-9\._]+)[\);]/.exec(ua)[1] 

	if /(Intel|PPC) Mac OS X/.test ua 
	then device.type.mac = (/(Intel|PPC) Mac OS X ?([0-9\._]*)[\)\;]/.exec(ua)[2].replace /_/g, '.' || true)
 
	if /like Mac OS X/.test ua 
	then device.type.ios = /CPU( iPhone)? OS ([0-9\._]+) like Mac OS X/.exec(ua)[2].replace /_/g, '.' 

	if /like Mac OS X/.test ua
	then device.type.iphone = /iPhone/.test ua 

	if /like Mac OS X/.test ua 
	then device.type.ipad = /iPad/.test ua 

	if /Android/.test ua 
	then device.type.android = /Android ([0-9\.]+)[\);]/.exec(ua)[1] 

	if /webOS\//.test ua 
	then device.type.webos = /webOS\/([0-9\.]+)[\);]/.exec(ua)[1] 

	device

module.exports.detect = detect