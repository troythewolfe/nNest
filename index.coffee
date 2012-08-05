#requires
express = require 'express'
buildRouter = require './lib/build_router.js'
client = require './lib/helpers/client.js'

app = express.createServer()

#defaults all non-defined get requests to the public folder
app.configure ->
	 app.use '/', express.static __dirname + '/public'

getApp = (req, res)->
	index = buildRouter.getIndex client.detect req
	res.send index

#app root
app.get '/', (req, res) ->
	getApp req, res

#app with view route
app.get '/view/*', (req, res) ->
	getApp req, res

#get requests
app.get '/fetch/:format/*', (req, res) ->
	format = req.params['format']
	res.send format

app.listen 2323