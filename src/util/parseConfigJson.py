import sys
import json
from Get import Get
import printError as error
sys.path.append('/')
get = Get()

def parseConfig(loc):
	def buildPath():
		path = ''
		configType = ''
		
		if 'profile' in loc:
			configType = loc['profile']
		else:
			configType = 'config'
		
		if ('page' in loc) and not ('view' in loc):
			path = 'pages/' + loc['page']
		elif ('page' in loc) and ('view' in loc):
			path = 'pages/' + loc['page'] + '/view/' + loc['view']
		elif not ('page' in loc) and ('view' in loc):
			path = 'views/' + loc['view']

		buildPath = {
			'path' : path,
			'profile' : configType
		}
		
		return buildPath;
	
	buildPath = buildPath()
	configPath = buildPath['path'] + '/' + buildPath['profile']
	
	try:
		config_string = open(configPath + '.json')
	except: 
		error.log('no file found at ' + configPath + '.json')
		return False
	
	try:
		config_json = json.load(config_string)
		config_string.close()
	except:
		error.log('badly formed json in ' + configPath + '.json')
		return False

	assetType = 'js'
	if assetType == 'js':
		for asset in config_json[assetType]:
			assetPath = {
				'location' : 'internal',
				'path' : False
			}
			
			if type(asset) is unicode:
				assetPath['path'] = buildPath['path'] + '/' + assetType + '/' + asset + '.' + assetType
			elif type(asset) is dict:
				if ('page' in asset) and ('view' in asset):
					assetPath['path'] = 'pages/' + asset['page'] + '/views/' + asset['view'] + '/' + assetType + '/' + asset[assetType] + '.' + assetType
				elif('page' in asset):
					assetPath['path'] = 'pages/' + asset['page'] + '/' + assetType + '/' + asset[assetType] + '.' + assetType
				elif('view' in asset):
					assetPath['path'] = 'views/' + asset['view'] + '/' + assetType + '/' + asset[assetType] + '.' + assetType
				elif('js' in asset):
					assetPath['path'] = assetType + '/' + asset[assetType] + '.' + assetType
				elif('ext' in asset):
					pass
					assetPath['path'] = asset['ext']
					assetPath['location'] = 'external'
			
			if assetPath['path'] is False:
				error.log('badly formed' + assetType + ' include in ' + configPath)
		
	return config_json


#print 'page:home'
#print '-------------------'
currConfig = parseConfig({
	'profile' : 'chromeWeb',
	'page' : 'home'
})

print currConfig
#print '-------------------'
#print ' '

"""
print 'page:home, view:nav'
print '-------------------'
print parseConfig({
	'page' : 'home',
	'view' : 'nav'
})

print '-------------------'
print ' '

print 'view:nav'
print '-------------------'
print parseConfig({
	'view' : 'nav'
})
print '-------------------'
print ' '
"""
