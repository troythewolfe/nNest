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

class Get():
	def __init__(self):
		pass
		
	def get(self, ext, fileName=False, options={}, viewPage=False, name=False, configType=False, viewType=False):
		jsPath = 'js/'
		cssPath = 'css/'
		htmlPath = 'html/'
		viewPath = 'views/'
		pagePath = 'pages/'
		indexPath = 'indexes/'
		langlPath = 'lang/'
		
		self.configType = configType
		self.viewType = viewType
		self.viewPage = viewPage
		self.name = name
		
		if fileName == False:
			fileName = self.name

		### CSS
		if ext == 'css':
			if options == {}:
				if self.configType == 'view':
					if self.viewPage == False:
						return css(fileName, 'view', self.name)
					else:
						return css(fileName, 'page', self.name, self.viewPage)
				elif self.configType == 'page':
					return css(fileName, 'page', self.name)
			else:
				if 'css' in options and (options['css'] == True):
					return css(fileName)
					
				if 'view' in options and not 'page' in options:
					return css(fileName, 'view', options['view'])
					
				if 'page' in options:
					if 'view' in options:
						return css(fileName, 'page', options['view'], options['page'])
					else:
						return css(fileName, 'page', options['page'])

		### JS
		if ext == 'js':
			if options == {}:
				if self.configType == 'view':
					if self.viewPage == False:
						return js(fileName, 'view', self.name)
					else:
						return js(fileName, 'page', self.name, self.viewPage)
				elif self.configType == 'page':
					return js(fileName, 'page', self.name)

			else:
				if 'js' in options and (options['js'] == True):
					return js(fileName)
					
				if 'view' in options and not 'page' in options:
					return js(fileName, 'view', options['view'])
					
				if 'page' in options:
					if 'view' in options:
						return js(fileName, 'page', options['view'], options['page'])
					else:
						return js(fileName, 'page', options['page'])

		### TEMPLATE
		if ext == 'html':
			templateExt = 'html'
			templatePath = ''
			returnTemplate = ''
			template = {
				'location' : '',
				'source' : 'foo',
				'fileName' : fileName,
				'type' : False,
				'html' : False,
				'page' : False,
				'view' : False
			}
			
			if options == {}:
				if self.viewPage == False:
					if self.configType == 'view':
						#return a path to view/viewname/html/filename.html
						returnTemplate = dict(template, **html(fileName, 'view', self.name))
						returnTemplate['type'] = 'view'
					elif self.configType == 'page':
						returnTemplate = dict(template, **html(fileName, 'page', self.name))
						returnTemplate['type'] = 'page'
				else:
					#return a path to pages/pageName/views/viewName/html/filename.html
					returnTemplate = dict(template, **html(fileName, 'page', self.name, self.viewPage))
					returnTemplate['type'] = 'page'
					returnTemplate['page'] = self.viewPage
					returnTemplate['view'] = self.name
				
			else:
				if 'html' in options:
					#return a path to html/folderName/filename.html
					returnTemplate = dict(template, **html(fileName, 'html', options['html']))
					returnTemplate['type'] = 'html'
					returnTemplate['html'] = options['html']
					
				if 'view' in options and not 'page' in options:
					#return a path to views/viewName/html/filename.html
					returnTemplate = dict(template, **html(fileName, 'view', options['view']))
					returnTemplate['type'] = 'view'
					returnTemplate['view'] = options['view']
						
				if 'page' in options: 
					if 'view' in options:
						#return a path to pages/pageName/views/viewName/html/filename.html
						returnTemplate = dict(template, **html(fileName, 'page', options['view'], options['page']))
						returnTemplate['type'] = 'page'
						returnTemplate['page'] = options['page']
						returnTemplate['view'] = options['view']
					else:
						#return a path to page/pageName/html/filename.html
						returnTemplate = dict(template, **html(fileName, 'page', options['page']))
						returnTemplate['type'] = 'page'
						returnTemplate['page'] = options['page']
			
			return returnTemplate
			
		### INDEX
		if ext == 'index':
			#convert variables
			ext = 'html'
			indexPage = fileName
			indexProfile = options

			filePath = indexPath + indexProfile + '-' + indexPage + '.' + ext
	
			htmlFile = {
				'location' : filePath,
				'source' : open(filePath).read()
			}

			return htmlFile
		
		### LANG
		if ext == 'lang':
					
			#def lang(fileName, type='', name=''):
			ext = 'json'
			return False
			'''
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
			'''	

