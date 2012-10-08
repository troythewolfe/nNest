def init(ua, request, pathParams={}):                              
	#default
	profileName = 'modernWeb'
	
	#legacyWeb
	if ua['user_agent']['family'] == "IE" and float(ua['user_agent']['major']) <= 7:
		profileName = 'legacyWeb'
		
	#chromeWeb
	if ua['user_agent']['family'] == "Chrome":
		profileName = 'chromeWeb'

	return profileName