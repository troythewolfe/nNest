from flask import Flask, request
import appSettings.router as router
import appSettings.profileParser as profileParser
import appSettings.profileList as profileList
from ua_parser import user_agent_parser

#create flask app object
app = Flask(__name__, static_path='/static')

#passed into router init and used there
#defined here to keep noise out of configurable file
def processPage(page, pathParams={}):
	#setup profile vars
	profiles = profileList.init()
	uaString = request.headers.get('User-Agent')
	ua = user_agent_parser.Parse(uaString)

	#determine current profileName
	profileName = profileParser.init(profiles, ua, request, pathParams={})

	#set profile object
	profile = {
		'name' : profileName,
		'ua' : ua,
		'path' : request.path,
		'pathParams' : pathParams
	}

	#get page html
	return page.init(profile)

#pass app object to page router
router.init(app, processPage)

if __name__ == '__main__':
    app.run()
