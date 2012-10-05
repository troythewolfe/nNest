import sys
sys.path.append('/')

def get(templateName):
	templatePath = 'templates/'
	templateExt = 'html'

	return open(templatePath + templateName + '.' + templateExt).read()