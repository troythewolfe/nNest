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

	for js in config_json['js']:
		print 'js---'
		print type(js)
		print js
		if type(js) is unicode:
			print 'is string ----'
			print js

	return config_json


print 'page:home'
print '-------------------'
print parseConfig({
	'profile' : 'chromeWeb',
	'page' : 'home'
})
print '-------------------'
print ' '

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
