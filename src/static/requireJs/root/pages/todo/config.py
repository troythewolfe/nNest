from util.configPage import ConfigPage

def init(profile):
	config = ConfigPage('todo')

	config.html = config.get('html')

	#config.jsInc =[
	#	config.set('js')
	#]

	return config
