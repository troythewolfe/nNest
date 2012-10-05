import sys
sys.path.append('/')

jsPath = 'js/'
cssPath = 'css/'
htmlPath = 'html/'
viewPath = 'views/'
pagePath = 'pages/'

def js(fileName, type='', name=''):
	ext = 'js'
	
	localJsPath = jsPath

	if type == 'view':
		localJsPath = viewPath + name + '/' + jsPath

	if type == 'page':
		localJsPath = pagePath + name + '/' + jsPath

	filePath = localJsPath + fileName + '.' + ext

	jsFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return jsFile

def css(fileName, type='', name=''):
	ext = 'css'

	localCssPath = cssPath

	if type == 'view':
		localCssPath = viewPath + name + '/' + cssPath

	if type == 'page':
		localCssPath = pagePath + name + '/' + cssPath

	filePath = localCssPath + fileName + '.' + ext

	cssFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return cssFile

def html(fileName, type='', name=''):
	ext = 'html'

	localHtmlPath = htmlPath

	if type == 'view':
		localHtmlPath = viewPath + name + '/' + htmlPath

	if type == 'page':
		localHtmlPath = pagePath + name + '/' + htmlPath

	filePath = localHtmlPath + fileName + '.' + ext

	htmlFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return htmlFile