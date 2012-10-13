import util.inc as inc

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
						return inc.css(fileName, 'view', self.name)
					else:
						return inc.css(fileName, 'page', self.name, self.viewPage)
				elif self.configType == 'page':
					return inc.css(fileName, 'page', self.name)
			else:
				if 'css' in options and (options['css'] == True):
					return inc.css(fileName)
					
				if 'view' in options and not 'page' in options:
					return inc.css(fileName, 'view', options['view'])
					
				if 'page' in options:
					if 'view' in options:
						return inc.css(fileName, 'page', options['view'], options['page'])
					else:
						return inc.css(fileName, 'page', options['page'])

		### JS
		if ext == 'js':
			if options == {}:
				if self.configType == 'view':
					if self.viewPage == False:
						return inc.js(fileName, 'view', self.name)
					else:
						return inc.js(fileName, 'page', self.name, self.viewPage)
				elif self.configType == 'page':
					return inc.js(fileName, 'page', self.name)

			else:
				if 'js' in options and (options['js'] == True):
					return inc.js(fileName)
					
				if 'view' in options and not 'page' in options:
					return inc.js(fileName, 'view', options['view'])
					
				if 'page' in options:
					if 'view' in options:
						return inc.js(fileName, 'page', options['view'], options['page'])
					else:
						return inc.js(fileName, 'page', options['page'])



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
						returnTemplate = dict(template, **inc.html(fileName, 'view', self.name))
						returnTemplate['type'] = 'view'
					elif self.configType == 'page':
						returnTemplate = dict(template, **inc.html(fileName, 'page', self.name))
						returnTemplate['type'] = 'page'
				else:
					#return a path to pages/pageName/views/viewName/html/filename.html
					returnTemplate = dict(template, **inc.html(fileName, 'page', self.name, self.viewPage))
					returnTemplate['type'] = 'page'
					returnTemplate['page'] = self.viewPage
					returnTemplate['view'] = self.name
				
			else:
				if 'html' in options:
					#return a path to html/folderName/filename.html
					returnTemplate = dict(template, **inc.html(fileName, 'html', options['html']))
					returnTemplate['type'] = 'html'
					returnTemplate['html'] = options['html']
					
				if 'view' in options and not 'page' in options:
					#return a path to views/viewName/html/filename.html
					returnTemplate = dict(template, **inc.html(fileName, 'view', options['view']))
					returnTemplate['type'] = 'view'
					returnTemplate['view'] = options['view']
						
				if 'page' in options: 
					if 'view' in options:
						#return a path to pages/pageName/views/viewName/html/filename.html
						returnTemplate = dict(template, **inc.html(fileName, 'page', options['view'], options['page']))
						returnTemplate['type'] = 'page'
						returnTemplate['page'] = options['page']
						returnTemplate['view'] = options['view']
					else:
						#return a path to page/pageName/html/filename.html
						returnTemplate = dict(template, **inc.html(fileName, 'page', options['page']))
						returnTemplate['type'] = 'page'
						returnTemplate['page'] = options['page']
			
			return returnTemplate

