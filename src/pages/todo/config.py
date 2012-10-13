import util.inc as inc
from util.configPage import ConfigPage
import os

def init(profile):
	config = ConfigPage('todo')

	config.html = config.get('html')

	#config.jsInc =[
	#	config.set('js')
	#]

	return config
