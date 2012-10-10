from flask import Flask, request
import appSettings.router as router
import appSettings.profileParser as profileParser
from ua_parser import user_agent_parser

#import for dev mode, remove for production
import build

SERVER_NAME = '127.0.0.1'
SERVER_PORT = 5000

#create flask app object
app = Flask(__name__, static_path='/static')

#passed into router init and used there
#defined here to keep noise out of configurable file
def processPage(page, pathParams={}):

	#parse user agent string
	ua = user_agent_parser.Parse(request.headers.get('User-Agent'))

	#determine current profile.name
	profileName = profileParser.init(ua, request, pathParams)

	#set profile object
	profile = {
		'name' : profileName,
		'ua' : ua,
		'path' : request.path,
		'pathParams' : pathParams,
		'lang' : request.headers.get('Accept-Language')
	}

	#get page html
	return page.init(profile)

#pass app object to page router
router.init(app, processPage)

if __name__ == '__main__':
    app.run(SERVER_NAME, SERVER_PORT)
