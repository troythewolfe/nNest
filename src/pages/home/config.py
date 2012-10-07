import util.inc as inc
from util.configPage import ConfigPage

def init(profile):
	config = ConfigPage('home')

	config.template = config.set('template')

	config.jsInc =[
		config.set('js')
	]