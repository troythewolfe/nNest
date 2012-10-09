import util.inc as inc
from util.configView import ConfigView
import os

def init(profile):
	config = ConfigView(os.path.abspath(__file__))

	config.jsInc =[
		config.get('js')
	]

	import views.footer.config as footer
	config.views ={
		'footer' : footer.init(profile)
	}

	return config