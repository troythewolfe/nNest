import json
import sys
sys.path.append('/')

jsPath = 'js/'
cssPath = 'css/'
htmlPath = 'html/'
viewPath = 'views/'
pagePath = 'pages/'
indexPath = 'indexes/'
langlPath = 'lang/'

def js(fileName, type='', name='', pageView=''):
	ext = 'js'
	
	localJsPath = jsPath

	if type == 'view':
		localJsPath = viewPath + name + '/' + jsPath

	if type == 'page':
		if pageView == '':
			localJsPath = pagePath + name + '/' + jsPath
		else:
			localJsPath = pagePath + pageView + '/views/' + name + '/' + jsPath

	filePath = localJsPath + fileName + '.' + ext

	jsFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return jsFile

def css(fileName, type='', name='', pageView=''):
	ext = 'css'

	localCssPath = cssPath

	if type == 'view':
		localCssPath = viewPath + name + '/' + cssPath

	if type == 'page':
		if pageView == '':
			localCssPath = pagePath + name + '/' + cssPath
		else:
			localCssPath = pagePath + pageView + '/views/' + name + '/' + cssPath

	filePath = localCssPath + fileName + '.' + ext

	cssFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return cssFile

def html(fileName, type='', name='', pageView=''):
	ext = 'html'

	localHtmlPath = htmlPath

	if type == 'view':
		localHtmlPath = viewPath + name + '/' + htmlPath

	if type == 'page':
		if pageView == '':
			localHtmlPath = pagePath + name + '/' + htmlPath
		else:
			localHtmlPath = pagePath + pageView + '/views/' + name + '/' + htmlPath

	if type == 'html':
		localHtmlPath = localHtmlPath + name + '/'

	filePath = localHtmlPath + fileName + '.' + ext

	htmlFile = {
		'source' : open(filePath).read(),
		'location' : filePath
	}

	return htmlFile


def template(fileName, name):
	templateExt = 'html'	

	filePath = htmlPath + name + '/' + fileName + '.' + templateExt

	htmlFile = {
		'location' : filePath,
		'source' : open(filePath).read(),
		'name' : fileName,
		'type' : 'html',
		'typeName' : name
	}

	return htmlFile

def index(page, profile):
	ext = 'html'

	filePath = indexPath + profile + '-' + page + '.' + ext
               
	htmlFile = {
		'location' : filePath,
		'source' : open(filePath).read()
	}

	return htmlFile

def lang(fileName, type='', name=''):
	ext = 'json'

	localLangPath = langlPath

	if type == 'view':
		localLangPath = viewPath + name + '/' + langlPath

	if type == 'page':
		localLangPath = pagePath + name + '/' + langlPath

	filePath = localLangPath + fileName + '.' + ext

	langFile = {
		'location' : filePath,
		'source' : json.load(open(filePath))
	}

	return langFile
