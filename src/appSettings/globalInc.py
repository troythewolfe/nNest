from util.configRoot import ConfigRoot
import util.inc as inc

#define global js, css and template includes
def init():
	config = ConfigRoot()

	'''
	config.jsInc = [
		'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
		inc.js('third-party/jquery-1.8.2'),
		inc.js('third-party/underscore-1.4.0'),
		inc.js('third-party/backbone-0.9.2')
	]

	config.cssInc = [
		'http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css',
		inc.css('main')
	]
	'''

	config.templates = [
		#inc.template('listItem', 'shared')
	]
	
	return config
