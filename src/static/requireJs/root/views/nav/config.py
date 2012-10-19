from util.configView import ConfigView
import os

#nav
def init(profile):
	config = ConfigView('nav')


	config.css = [
		config.get('css')
	]
	
	#subdirs as part of file name are not allowed, and therefore further directory nesting is not allowed
	config.templates = [
		#call template in local folder with name of view
		config.get('html')
	]

	import views.footer.config as footer
	config.views = {
		'footer' : footer.init(profile)
	}

	return config
