import profileList
from ua_parser import user_agent_parser

def init(request, pathParams={}):
	profiles = profileList.init()

	uaString = request.headers.get('User-Agent')
	ua = user_agent_parser.Parse(uaString)

	#### START PROFILE CONDITIONS ####

	#set the default profile name
	profileName = profiles['modernWeb']
	
	#unsupported conditional
	if ua['user_agent']['family'] == "IE" and float(ua['user_agent']['major']) <= 7:
		profileName = profiles['legacyWeb']
		
	#chrome conditional
	if ua['user_agent']['family'] == "Chrome":
		profileName = profiles['chromeWeb']
	
	#### END PROFILE CONDITIONS ####

	profile = {
		'name' : profileName,
		'ua' : ua,
		'path' : request.path,
		'pathParams' : pathParams
	}

	return profile