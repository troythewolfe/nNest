from util.configPage import ConfigPage

#page/home
def init(profile):
	config = ConfigPage('home')

	config.html = config.get('html')
	config.head['title'] = 'home page title set here'
	
	#config.baseTemplate = 'ajax'
	
	config.cssInc = [
		config.get('css')
	]

	config.jsInc = [
		config.get('js')
	]
	
	#subdirs as part of file name are not allowed, and therefore further directory nesting is not allowed
	config.templates = [
		#call template in local folder with name of view
		config.get('html')
	]

	import pages.home.views.nav.config as homeNav
	config.views ={
		'homeNav' : homeNav.init(profile)
	}

	return config
