def init(profiles, ua, request, pathParams={}):                              
	#default
	profileName = profiles['modernWeb']
	
	#legacyWeb
	if ua['user_agent']['family'] == "IE" and float(ua['user_agent']['major']) <= 7:
		profileName = profiles['legacyWeb']
		
	#chromeWeb
	if ua['user_agent']['family'] == "Chrome":
		profileName = profiles['chromeWeb']

	return profileName