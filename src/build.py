from util.Get import html 
import util.parseConfigJson as parseConfig
import pystache
import copy
import json
import shutil
import os
import sys
import re
sys.path.append('/')

APP_JS_NAMESPACE = 'ns'
HTML_TEMPLATES_JS_NAMESPACE = 'templates'

class Build():
	def __init__(self):
		self.externalJsInc = []
		
		def getJson():
			#get globals
			global_string = open('appSettings/globals.json')
			self.g = json.load(global_string)
			global_string.close()
			
			#get profile array
			profile_string = open('appSettings/profiles.json')
			self.profiles = json.load(profile_string)
			profile_string.close()
			self.profiles = self.profiles['profiles']
			
			#get pages
			pages_string = open('appSettings/pages.json')
			self.pages = json.load(pages_string)
			self.pages = self.pages['pages']
			pages_string.close()
		
		def clearStaticDir():
			#empty generated dirs
			indexDir = 'indexes'
			if os.path.isdir(indexDir):
				shutil.rmtree(indexDir)
			os.mkdir(indexDir)

			cssDir = 'static/css'
			if os.path.isdir(cssDir):
				shutil.rmtree(cssDir)
			os.mkdir(cssDir)

			#clone assets into static
			staticRootJs = 'static/requireJs/root/js'
			if os.path.isdir(staticRootJs):
				shutil.rmtree(staticRootJs)
			shutil.copytree('js', 'static/requireJs/root/js/')

			staticRootViews = 'static/requireJs/root/views'
			if os.path.isdir(staticRootViews):
				shutil.rmtree(staticRootViews)
			shutil.copytree('views', 'static/requireJs/root/views/')

			staticRootPages = 'static/requireJs/root/pages'
			if os.path.isdir(staticRootPages):
				shutil.rmtree(staticRootPages)
			shutil.copytree('pages', 'static/requireJs/root/pages/')

			staticHTML = 'static/requireJs/html'
			if os.path.isdir(staticHTML):
				shutil.rmtree(staticHTML)
			shutil.copytree('html', 'static/requireJs/html/')

			#remove files from asset root, but leave directories
			folder = 'static/requireJs'
			for the_file in os.listdir(folder):
				file_path = os.path.join(folder, the_file)
				try:
					if os.path.isfile(file_path):
						os.unlink(file_path)
				except Exception, e:
					print e

		def buildGlobalIncs():
			self.globalInc = parseConfig.parseConfig({
				'global' : 'true'
			})
			
			#set globalInc properties
			#used to build the global js and css files
			self.globalConfig = {
				'js' : [],
				'css' : [],
				'html' : []
			}
			
			if  hasattr(self.globalInc, 'js'):
				self.globalConfig['js'] = self.globalInc.js
			
			if  hasattr(self.globalInc, 'css'):
				self.globalConfig['css'] = self.globalInc.css
			
			if  hasattr(self.globalInc, 'html'):
				self.globalConfig['html'] = self.globalInc.html

			globalJsInc = 'static/requireJs/global.js'
			jsFile = open(globalJsInc, 'w+')
			jsFile.write(self.renderJS(self.globalConfig['js'], self.globalConfig['html'])) 

			mainCssInc = 'static/css/global.css'
			cssFile = open(mainCssInc, 'w+')
			cssFile.write(self.renderCSS(self.globalConfig['css']))

		getJson()
		clearStaticDir()
		buildGlobalIncs()

		#loop over each profile
		for profile in self.profiles:
			#set the current profile
			self.profile = profile

			#loop over each page listed in config
			for page in self.pages:				
				#by default send down en lang package
				#if en is ever no longer the majority of traffic, this can be removed
				self.config = parseConfig.parseConfig({
					'lang' : 'en',
					'profile' : profile,
					'page' : page
				})
				
				if self.config is False:
					self.config = parseConfig.parseConfig({
						'lang' : 'en',
						'profile' : 'config',
						'page' : page
					})
				
				#apply global config
				if hasattr(self.config, 'baseTemplate'):
					self.baseTemplate = self.config.baseTemplate
				else:
					self.baseTemplate = 'base'
				
				self.js = []
				for jsInc in self.globalConfig['js']:
					if not isinstance(jsInc, dict):
						self.js.append(jsInc)

				self.js.extend(copy.copy(self.config.js))
			
				self.css = []
				for cssInc in self.globalConfig['css']:
					if not isinstance(cssInc, dict):
						self.css.append(cssInc)

				self.css.extend(copy.copy(self.config.css))
				
				self.htmlTemplates = []
				
				self.views = copy.copy(self.config.views)
				
				self.head = {
					'title' : 'Where should i store the default title?'
				}
				
				self.pageTemplate = '{{{content}}}'
								
				#apply page config
				self.applyPageConfig(self.config, self)
	
				#apply view configs
				if self.views:
					for view in self.views:																		
						if type(view is unicode):
							print 'page ============'
							print page
							
							view = {
								'view' : view,
								'page' : page
							}
						
						currLoc = {
							'lang' : 'en',
							'profile' : profile
						}
						
						currView = dict(currLoc, **view)
						
						currViewConfig = parseConfig.parseConfig(currView)
						
						self.applyViewConfigs(currViewConfig, self)
				
				#render page
				self.render(self.pageTemplate, self.pageName, self.profile)
	
	#overwrite defaults and add page specific configs
	def applyPageConfig(self, pageConfig, curr):
		if 'title' in pageConfig.head:
			curr.head['title'] = copy.copy(pageConfig.head['title'])
	
		if hasattr(pageConfig, 'baseTemplate'):
			curr.baseTemplate = copy.copy(pageConfig.baseTemplate)	
		
		if hasattr(pageConfig, 'jsInc'):
			curr.js.extend(copy.copy(pageConfig.jsInc))

		if hasattr(pageConfig, 'cssInc'):
			curr.css.extend(copy.copy(pageConfig.cssInc))

		if hasattr(pageConfig, 'templates'):
			curr.htmlTemplates.extend(copy.copy(pageConfig.templates))
		
		if hasattr(pageConfig, 'html'):
			curr.pageTemplate = copy.copy(pageConfig.html)

		if hasattr(pageConfig, 'name'):
			curr.pageName = copy.copy(pageConfig.name)

		if hasattr(pageConfig, 'views'):
			for nestedView in pageConfig.views:
				curr.applyViewConfigs(nestedView, curr)

	#add includes to config for current profile/page
	def applyViewConfigs(self, viewConfig, curr):
		if hasattr(viewConfig, 'jsInc'):
			curr.js.extend(copy.copy(viewConfig.jsInc))

		if hasattr(viewConfig, 'cssInc'):
			curr.js.extend(copy.copy(viewConfig.cssInc))

		if hasattr(viewConfig, 'templates'):
			curr.htmlTemplates.extend(copy.copy(viewConfig.templates))

		if hasattr(viewConfig, 'views'):
			for nestedView in viewConfig.views:
				curr.applyViewConfigs(nestedView, curr)

	#render htmlInc into js html templates
	def renderTemplates(self, htmlTemplates):
		def processSource(sourceStr):
			strippedSource = sourceStr.replace('\n', '')
			strippedSource = strippedSource.replace('\r', '')
			strippedSource = strippedSource.replace('\t', ' ')
			strippedSource = strippedSource.replace('"', '\\"')
			return strippedSource
		
		#set up base string/namespace
		templateString = 'window.' + APP_JS_NAMESPACE + ' = {};\n'
		templatePrepend = 'window.' + APP_JS_NAMESPACE + '.'
		templatePrepend = templatePrepend + HTML_TEMPLATES_JS_NAMESPACE
		templateString += templatePrepend + ' = {};\n'
		
		#use for view
		templateViewPrepend = templatePrepend + '.view'
		templateString += templateViewPrepend + ' = {};\n'
		
		#use for page
		templatePagePrepend = templatePrepend + '.page'
		templateString += templatePagePrepend + ' = {};\n'
		
		#use for html
		templateHTMLPrepend = templatePrepend + '.html'
		templateString += templateHTMLPrepend + ' = {};\n'
		
		templateRoots = []

		#loop over to determine html/folders and types
		templateTypes = {}
		for htmlTemplate in htmlTemplates:			
			if not (htmlTemplate['html'] == False):
				if not (htmlTemplate['html'] == True):
					templateRoots.append(templateHTMLPrepend + '.' + htmlTemplate['html'] + ' = {};\n')
		
			if not (htmlTemplate['view'] == False) and (htmlTemplate['page'] == False):
				templateRoots.append(templateViewPrepend + '.' + htmlTemplate['view'] + ' = {};\n')
				
			if not (htmlTemplate['page'] == False):
				templateRoots.append(templatePagePrepend + '.' + htmlTemplate['page'] + ' = {};\n')
				
				if not (htmlTemplate['view'] == False):
					templateRoots.append(templatePagePrepend + '.' + htmlTemplate['page'] + '.' + htmlTemplate['view'] + ' = {};\n')	
		
		dedupedTemplateRoots = []
		
		for rootTemplate in templateRoots:
			if rootTemplate not in dedupedTemplateRoots:
				dedupedTemplateRoots.append(rootTemplate)
		
		for rootTemplate in dedupedTemplateRoots:
			templateString += rootTemplate
				
		for htmlTemplate in htmlTemplates:
			if not (htmlTemplate['html'] == False):
				if not (htmlTemplate['html'] == True):
					templateString += templateHTMLPrepend + '.' + htmlTemplate['html'] + '.' + htmlTemplate['fileName'] + ' = "' + processSource(htmlTemplate['source']) + '";\n'
				else:
					templateString += templateHTMLPrepend + '.' + htmlTemplate['fileName'] + ' = "' + processSource(htmlTemplate['source']) + '";\n'
		
			if not (htmlTemplate['view'] == False) and (htmlTemplate['page'] == False):
				templateString += templateViewPrepend + '.' + htmlTemplate['view'] + '.' + htmlTemplate['fileName'] + ' = "' + processSource(htmlTemplate['source']) + '";\n'
			
			if not (htmlTemplate['page'] == False):
				if (htmlTemplate['view'] == False):
					templateString += templatePagePrepend + '.' + htmlTemplate['page'] + '.' + htmlTemplate['fileName'] + ' = "' + processSource(htmlTemplate['source']) + '";\n'
				else:
					templateString += templatePagePrepend + '.' + htmlTemplate['page'] + '.' + htmlTemplate['view'] + '.' + htmlTemplate['fileName'] + ' = "' + processSource(htmlTemplate['source']) + '";\n'
		
		return templateString

	#compiles local js
	def renderJS(self, jsFiles, htmlTemplates):
		jsInc = ''
		for jsFile in jsFiles:
			if isinstance(jsFile, dict) and not (jsFile['local'] is False):
				jsInc += jsFile['source'] + '\n'
		
		jsInc += self.renderTemplates(htmlTemplates)

		return jsInc

	#puts all external js files into an object
	def getJS(self):
		externalJsInc = []
		for jsFile in self.js:
			if not isinstance(jsFile, dict):
				externalJsInc.append({ 'url' : jsFile })

		orderedExtJsInc = []
		for externalJs in externalJsInc:
			if externalJs['url'][0] != '/':
				orderedExtJsInc.append(externalJs)

		return orderedExtJsInc

	#compiles local css
	def renderCSS(self, cssFiles):
		cssInc = ''
		for cssFile in cssFiles:
			if isinstance(cssFile, dict) and not (cssFile['local'] is False):
				cssInc += cssFile['source'] + '\n'
	  
		return cssInc

	#puts all external css files into an object
	def getCSS(self):
		externalCssInc = []
		for cssFile in self.css:
			if not isinstance(cssFile, dict):
				externalCssInc.append({ 'url' : cssFile })
	
		orderedExtCssInc = []
		for externalCss in externalCssInc:
			if externalCss['url'][0] != '/':
				orderedExtCssInc.append(externalCss)			

		for externalCss in externalCssInc:
			if externalCss['url'][0] == '/':
				orderedExtCssInc.append(externalCss)
			
		return orderedExtCssInc
	
	#render index
	def render(self, content, pageName, profile):
		#add generated js/css files to lists
		profilePage = profile + '-' + pageName['page']		

		mainJsInc = 'static/requireJs/' + profilePage + '.js'
		jsFile = open(mainJsInc, 'w+')
		jsFile.write(self.renderJS(self.js, self.htmlTemplates))

		mainCssInc = 'static/css/' + profilePage + '.css'
		cssFile = open(mainCssInc, 'w+')
		cssFile.write(self.renderCSS(self.css))

		if isinstance(content, dict):
			content = content['source']

		#assing template variables
		templateContent = {
			'title' : self.head['title'],
			'profilePage' : profilePage,
			'jsInc' : self.getJS(),
			'cssInc' : self.getCSS(),
			'bodyContent' : content
		}

		#create index file
		indexFile = open('indexes/' + profilePage + '.html', 'w+')
		pageTemplate = html(self.baseTemplate)
		#print pageTemplate['source']
		indexFile.write(pystache.render(pageTemplate['source'], templateContent))

build = Build()
