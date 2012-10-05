import sys
sys.path.append('/')

pagesPath = 'pages/'

def html(pageName, fileName):
	path = '/html/'
	ext = 'html'

	return open(pagesPath + pageName + path + fileName + '.' + ext).read()

def css(pageName, fileName):
	path = '/css/'
	ext = 'css'

	filePath = pagesPath + pageName + path + fileName + '.' + ext

	cssFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return cssFile

def js(pageName, fileName):
	path = '/js/'
	ext = 'js'

	filePath = pagesPath + pageName + path + fileName + '.' + ext

	jsFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return jsFile