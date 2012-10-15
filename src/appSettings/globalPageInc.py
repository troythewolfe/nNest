from util.configRoot import ConfigRoot

#define global js, css and template includes
def init():
	config = ConfigRoot()

	config.jsInc = [
		'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
		config.get('js', 'third-party/jquery-1.8.2', {
			'js' : True
		}),
		config.get('js', 'third-party/underscore-1.4.0', {
			'js' : True
		}),
		config.get('js', 'third-party/backbone-0.9.2', {
			'js' : True
		})
	]

	config.cssInc = [
		'http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css',
		config.get('css', 'main', {
			'css' : True
		})
	]
	
	'''
	Alternative syntax:
	
	config.require({
		...
	},{
		...
	},{
		...
	},{
		...
	})
	
	{
		'type' : 'string' //'html', 'css', 'js', 'lang'
		'file' : '',
		'css' : '',
		'js' : '',
		'html' : '',
		'lang' : '',
		'page' : '',
		'view' : ''
	}
	'''
	
	return config
