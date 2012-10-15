from util.configPage import ConfigPage

def init(profile):
	config = ConfigPage('calendar')

	config.html = config.get('html')
	config.head['title'] = 'home page title set here'
	'''
	config.jsInc =[
		config.get('js')
	]
	'''
	
	return config
