import util.inc as inc

class Get():
	def __init__(self):
		pass
		
	def get(self, ext, fileName=False, options={}):
		jsPath = 'js/'
		cssPath = 'css/'
		htmlPath = 'html/'
		viewPath = 'views/'
		pagePath = 'pages/'
		indexPath = 'indexes/'
		langlPath = 'lang/'

		if not hasattr(self, 'viewPage'):
			self.viewPage = False
		
		if fileName == False:
			fileName = self.name


		### CSS
		if ext == 'css':
			if options == {}:
				if self.viewType == 'view':
					if self.viewPage == False:
						return inc.css(fileName, 'view', self.name)
					else:
						return inc.css(fileName, 'page', self.name, self.viewPage)
				elif self.viewType == 'page':
					return inc.css(fileName, 'page', self.name)
			else:
				if options['type'] == 'css':
					return inc.css(fileName)
					
				if options['type'] == 'view':
					return inc.css(fileName, 'view', self.name)
					
				if options['type'] == 'page':
					if 'view' in options:
						return inc.css(fileName, 'page', options['view'], options['page'])
					else:
						return inc.css(fileName, 'page', options['page'])

		### JS
		if ext == 'js':
			if options == {}:
				if self.viewPage == False:
					return inc.js(fileName, 'view', self.name)
				else:
					return inc.js(fileName, 'page', self.name, self.viewPage)

			else:
				if options['type'] == 'js':
					return inc.js(fileName)
					
				if options['type'] == 'view':
					return inc.js(fileName, 'view', self.name)
					
				if options['type'] == 'page':
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
					#return a path to view/viewname/html/filename.html
					returnTemplate = dict(template, **inc.html(fileName, 'view', self.name))
					returnTemplate['type'] = 'view'
				else:
					#return a path to pages/pageName/views/viewName/html/filename.html
					returnTemplate = dict(template, **inc.html(fileName, 'page', self.name, self.viewPage))
					returnTemplate['type'] = 'page'
					returnTemplate['page'] = self.viewPage
					returnTemplate['view'] = self.name
				
			else:
				if options['type'] == 'html':
					if 'html' in options:
						#return a path to html/folderName/filename.html
						returnTemplate = dict(template, **inc.html(fileName, 'html', options['html']))
						returnTemplate['type'] = 'html'
						returnTemplate['html'] = options['html']
					else:
						print 'Error: you cannot include templates from the root of src/html/'
			
				if options['type'] == 'view':
					if 'view' in options:
						#return a path to views/viewName/html/filename.html
						returnTemplate = dict(template, **inc.html(fileName, 'view', options['view']))
						returnTemplate['type'] = 'view'
						returnTemplate['view'] = options['view']
					else:
						print 'Error: you cannot include templates from the root of src/views/'
			
				if options['type'] == 'page':
					if 'page' in options and not ('view' in options):
						#return a path to page/pageName/html/filename.html
						returnTemplate = dict(template, **inc.html(fileName, 'page', options['page']))
						returnTemplate['type'] = 'page'
						returnTemplate['page'] = options['page']
					elif ('page' in options) and ('view' in options):
						#return a path to pages/pageName/views/viewName/html/filename.html
						returnTemplate = dict(template, **inc.html(fileName, 'page', options['view'], options['page']))
						returnTemplate['type'] = 'page'
						returnTemplate['page'] = options['page']
						returnTemplate['view'] = options['view']
			
			return returnTemplate

