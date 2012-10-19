from util.configRoot import ConfigRoot

#define global js, css and template includes
def init():
	config = ConfigRoot()

	config.jsInc = [
		config.get('js', 'third-party/require-min', {
			'js' : True
		}),
		config.get('js', 'requireConfig', {
			'js' : True
		}),
	]

	config.cssInc = [
		#'http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css',
		config.get('css', 'main', {
			'css' : True
		})
	]
	
	return config
