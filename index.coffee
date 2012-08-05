#requires
express = require 'express'
_ = require 'underscore'
builds = require './lib/builds.js'
device = require './lib/helpers/device.js'

app = express.createServer()

#defaults all non-defined get requests to the public folder
app.configure ->
	 app.use '/', express.static __dirname + '/public'

#app root
app.get '/', (req, res) ->
	index = builds.route device.detect req
	res.send index

#app with view route
app.get '/view/*', (req, res) ->
	index = builds.route device.detect req
	res.send index

#get requests
app.get '/fetch/:format/', (req, res) ->
	format = req.params['format']
	res.send format

app.listen 2323