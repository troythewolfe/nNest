import util.inc as inc
from util.configPage import ConfigPage
import os

def init(profile):
	config = ConfigPage(os.path.abspath(__file__))

	config.html = config.get('html')
	config.head['title'] = 'home page title set here'
	'''
	config.jsInc =[
		config.get('js')
	]
	'''
	
	return config
