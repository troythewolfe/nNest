import util.inc as inc
import appSettings.config as config
import appSettings.profileList as profileList
import pystache
import copy
import shutil
import os
import sys
import re
sys.path.append('/')

HTML_TEMPLATES_NAMESPACE = 'templates'

class Build():
	def __init__(self):
		#empty generated dirs
		indexDir = 'indexes'
		if os.path.isdir(indexDir):
			shutil.rmtree(indexDir)
		os.mkdir(indexDir)

		jsDir = 'static/js'
		if os.path.isdir(jsDir):
			shutil.rmtree(jsDir)
		os.mkdir(jsDir)

		cssDir = 'static/css'
		if os.path.isdir(cssDir):
			shutil.rmtree(cssDir)
		os.mkdir(cssDir)

		#get registered profiles
		self.profiles = profileList.init()

		#build global includes
		self.globalInc = config.globalInc()

		#print self.globalInc.jsInc

		self.externalJsInc = []
		self.globals = {}
		self.globals['js'] = copy.copy(self.globalInc.jsInc)
		self.globals['css'] = copy.copy(self.globalInc.cssInc)
		self.globals['htmlTemplates'] = copy.copy(self.globalInc.templates)

		globalJsInc = 'static/js/global.js'
		jsFile = open(globalJsInc, 'w+')
		jsFile.write(self.renderJS(self.globals['js'], self.globals['htmlTemplates']))
		globalJsPath = '/' + globalJsInc
	
		print globalJsPath

		mainCssInc = 'static/css/global.css'
		cssFile = open(mainCssInc, 'w+')
		cssFile.write(self.renderCSS(self.globals['css']))
		globalCssPath = '/' + mainCssInc

		#loop over each profile
		for profile in self.profiles:
			#set the current profile
			self.profile = profile

			#init the config based on current profile
			self.config = config.profile(self.profile)

			#loop over each page listed in config
			for pageConfig in self.config.pages:
				#apply global config
				self.baseTemplate = copy.copy(self.config.baseTemplate)
				self.js = []
				self.js.append(globalJsPath)
				self.js.extend(copy.copy(self.config.jsInc))
				self.css = []
				self.css.append(globalCssPath)
				self.css.extend(copy.copy(self.config.cssInc))
				self.htmlTemplates = copy.copy(self.config.templates)
				self.views = copy.copy(self.config.views)
				self.head = {
					'title' : copy.copy(self.config.head['title'])
				}
				self.pageTemplate = '{{{content}}}'
				
				#apply page config
				self.applyPageConfig(self.config.pages[pageConfig])
	
				#apply view configs
				if self.views:
					for view in self.views:
						self.applyViewConfigs(self.views[view])
				
				#render page
				self.render(self.pageTemplate, self.pageName, self.profile)
	
	#overwrite defaults and add page specific configs
	def applyPageConfig(self, pageConfig):
		if 'title' in pageConfig.head:
			self.head['title'] = copy.copy(pageConfig.head['title'])
	
		if hasattr(pageConfig, 'baseTemplate'):
			self.baseTemplate = copy.copy(pageConfig.baseTemplate)	
		
		if hasattr(pageConfig, 'jsInc'):
			self.js.extend(copy.copy(pageConfig.jsInc))

		if hasattr(pageConfig, 'cssInc'):
			self.css.extend(copy.copy(pageConfig.cssInc))

		if hasattr(pageConfig, 'templates'):
			self.htmlTemplates.extend(copy.copy(pageConfig.templates))
		
		if hasattr(pageConfig, 'html'):
			self.pageTemplate = copy.copy(pageConfig.html)

		if hasattr(pageConfig, 'name'):
			self.pageName = copy.copy(pageConfig.name)

		if hasattr(pageConfig, 'views'):
			for nestedView in pageConfig.views:
				self.applyViewConfigs(pageConfig.views[nestedView])

	def applyViewConfigs(self, viewConfig):
		if hasattr(viewConfig, 'jsInc'):
			self.js.extend(copy.copy(viewConfig.jsInc))

		if hasattr(viewConfig, 'cssInc'):
			self.js.extend(copy.copy(viewConfig.cssInc))

		if hasattr(viewConfig, 'templates'):
			self.htmlTemplates.extend(copy.copy(viewConfig.templates))

		if hasattr(viewConfig, 'views'):
			for nestedView in viewConfig.views:
				self.applyViewConfigs(viewConfig.views[nestedView])

	#render htmlInc into js html templates
	def renderTemplates(self, htmlTemplates):
		#print htmlTemplates

		#set up base string/namespace
		templatePrepend = 'window.' + HTML_TEMPLATES_NAMESPACE
		templateString = templatePrepend + ' = {};\n'

		typePrepend = {}
		typeOutputPrepend = {}

		#loop over to determine html/folders and types
		templateTypes = {}
		for htmlTemplate in htmlTemplates:
			templateTypes[htmlTemplate['type']] = {}
		
		for type in templateTypes:
			templateString += templatePrepend + '.' + type + ' = {};\n'
			for htmlTemplate in htmlTemplates:
				if htmlTemplate['type'] == type: 
					templateString += templatePrepend + '.' + type + '.'  + htmlTemplate['typeName'] + ' = {};\n'
					templateTypes[type][htmlTemplate['typeName']] = templatePrepend + '.' + type + '.' + htmlTemplate['typeName']


		for htmlTemplate in htmlTemplates:
			strippedSource = htmlTemplate['source'].replace('\n', '')
			strippedSource = strippedSource.replace('"', '\\"')
			templateString += templateTypes[htmlTemplate['type']][htmlTemplate['typeName']] + '.' + htmlTemplate['name'] + ' = "' + strippedSource + '";\n'

		return templateString

	#compiles local js
	def renderJS(self, jsFiles, htmlTemplates):
		jsInc = ''
		for jsFile in jsFiles:
			if isinstance(jsFile, dict):
				jsInc += jsFile['source'] + '\n'
		
		jsInc += self.renderTemplates(htmlTemplates)

		return jsInc

	#puts all external js files into an object
	def getJS(self):
		externalJsInc = []
		for jsFile in self.js:
			if not isinstance(jsFile, dict):
				externalJsInc.append({ 'url' : jsFile })

		return externalJsInc

	def renderCSS(self, cssFiles):
		cssInc = ''
		for cssFile in cssFiles:
			if isinstance(cssFile, dict):
				cssInc += cssFile['source'] + '\n'
	
		return cssInc

	#puts all external js files into an object
	def getCSS(self):
		externalCssInc = []
		for cssFile in self.css:
			if not isinstance(cssFile, dict):
				externalCssInc.append({ 'url' : cssFile })
	
		#print externalCssInc
			
		return externalCssInc
	
	#render index
	def render(self, content, pageName, profile):
		#add generated js/css files to lists
		profilePage = profile + '-' + pageName		

		mainJsInc = 'static/js/' + profilePage + '-min.js'
		jsFile = open(mainJsInc, 'w+')
		jsFile.write(self.renderJS(self.js, self.htmlTemplates))
		self.js.append('/' + mainJsInc)

		mainCssInc = 'static/css/' + profilePage + '-min.css'
		cssFile = open(mainCssInc, 'w+')
		cssFile.write(self.renderCSS(self.css))
		self.css.append('/' + mainCssInc)

		if isinstance(content, dict):
			content = content['source']

		print self.getCSS()

		#assing template variables
		templateContent = {
			'title' : self.head['title'],
			'jsInc' : self.getJS(),
			'cssInc' : self.getCSS(),
			'bodyContent' : content
		}

		#create index file
		indexFile = open('indexes/' + profilePage + '.html', 'w+')
		pageTemplate = inc.html(self.baseTemplate)
		indexFile.write(pystache.render(pageTemplate['source'], templateContent))

build = Build()