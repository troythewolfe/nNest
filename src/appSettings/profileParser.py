import profileList
from ua_parser import user_agent_parser

def init(request, pathParams={}):
	print 'profileParser'


	profiles = profileList.init()
	uaString = request.headers.get('User-Agent')
	ua = user_agent_parser.Parse(uaString)
                                 
	#default
	profileName = profiles['modernWeb']
	
	#legacyWeb
	if ua['user_agent']['family'] == "IE" and float(ua['user_agent']['major']) <= 7:
		profileName = profiles['legacyWeb']
		
	#chromeWeb
	if ua['user_agent']['family'] == "Chrome":
		profileName = profiles['chromeWeb']

	profile = {
		'name' : profileName,
		'ua' : ua,
		'path' : request.path,
		'pathParams' : pathParams
	}

	return profile
