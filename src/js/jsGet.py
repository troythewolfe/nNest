import sys
sys.path.append('/')

jsPath = 'js/'

def js(fileName):
	ext = 'js'

	filePath = jsPath + fileName + '.' + ext

	jsFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return jsFile