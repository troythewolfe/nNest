import util.inc as inc
from util.configView import ConfigView
import os

#nav
def init(profile):
	config = ConfigView(os.path.abspath(__file__))

	config.jsInc = [
		config.get('js')
	]

	config.htmlInc = [
		config.get('template', 'navItem'),
		config.get('template', 'listItem', 'shared'),
		config.get('template', 'listItem1', 'shared'),
		config.get('template', 'main', 'buttons')
	]

	import views.footer.config as footer
	config.views = {
		'footer' : footer.init(profile)
	}

	return config