import sys
import json
from Get import Get
from configPage import ConfigPage
from configView import ConfigView
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
	
	def parseFile(configPath):
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
			
		return config_json

	def parseAssets(config_json, curr_config):
		def getAsset(assetType):
			currAsset = []
			
			for asset in config_json[assetType]:
				assetPath = {
					'local' : True,
					'path' : False
				}
				
				assetExt = assetType
						
				if type(asset) is unicode:
					if assetType == 'lang':
						assetName = asset + '/' + loc['lang']
						assetExt = 'json'
					else:
						assetName = asset
						
					assetPath['path'] = buildPath['path'] + '/' + assetType + '/' + assetName + '.' + assetExt
				
				elif type(asset) is dict:
					if assetType == 'lang':
						assetName = asset[assetType] + '/' + loc['lang']
						assetExt = 'json'
					elif assetType in asset:
							assetName = asset[assetType]
						
					if ('dir' in asset):
						assetPath['path'] = assetType + '/' + asset['dir'] + '/' + assetName +  '.' + assetExt
					
					elif ('page' in asset) and ('view' in asset):
						assetPath['path'] = 'pages/' + asset['page'] + '/views/' + asset['view'] + '/' + assetType + '/' + assetName + '.' + assetExt
					
					elif('page' in asset):
						assetPath['path'] = 'pages/' + asset['page'] + '/' + assetType + '/' + assetName + '.' + assetExt
					
					elif('view' in asset):
						assetPath['path'] = 'views/' + asset['view'] + '/' + assetType + '/' + assetName + '.' + assetExt
					
					elif(assetType in asset):
						assetPath['path'] = assetType + '/' + assetName + '.' + assetExt
						
					elif('ext' in asset):
						assetPath['path'] = asset['ext']
						assetPath['local'] = False
						
				if assetPath['path'] is False:
					error.log('badly formed ' + assetType + ' include in ' + buildPath['path'] + '/' + buildPath['profile'])
				
				if (assetType == 'html' or assetType == 'lang'):
					if type(asset) is unicode:
						assetPath['name'] = asset
						
						if 'page' in loc:
							assetPath['page'] = loc['page']
							
						if 'view' in loc:
							assetPath['view'] = loc['view']
						
					elif type(asset) is dict:
						if ('dir' in asset):
							assetPath['dir'] = asset['dir']
							
						elif ('page' in asset) and ('view' in asset):
							assetPath['page'] = asset['page']
							assetPath['view'] = asset['view']
							
						elif('page' in asset):
							assetPath['page'] = asset['page']
							
						elif('view' in asset):
							assetPath['view'] = asset['view']
				
				if not 'ext' in asset:
					try:
						assetPath['source'] = open(assetPath['path']).read()
					except: 
						error.log('no file found at ' + assetPath['path'])					
				
				currAsset.append(assetPath)
			
			return currAsset
			
		curr_config.jsInc = getAsset('js')
		curr_config.cssInc = getAsset('css')
		curr_config.htmlInc = getAsset('html')
		curr_config.langInc = getAsset('lang')
		
		print curr_config.jsInc
		print '-----'
		print ' '
		
		print curr_config.cssInc
		print '-----'
		print ' '
		
		print curr_config.htmlInc
		print '-----'
		print ' '
		
		print curr_config.langInc
		print '-----'
		print ' '
		
		return curr_config
		
	#build path based on loc
	buildPath = buildPath()
	
	#get config json file based on buildPath
	configJson = parseFile(buildPath['path'] + '/' + buildPath['profile'])

	#instantiate base config class
	if ('view' in loc):
		currConfig = ConfigPage(loc)
	else:
		currConfig = ConfigView(loc)

	#parse assets and return populated config class
	return parseAssets(configJson, currConfig)


#print 'page:home'
#print '-------------------'
currConfig = parseConfig({
	'lang' : 'en',
	'profile' : 'chromeWeb',
	'page' : 'home'
})

#print currConfig
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
