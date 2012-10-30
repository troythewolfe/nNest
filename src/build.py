import appSettings.configPages as configPages
from util.Get import html 
import appSettings.globalPageInc as globalInc
import util.parseConfigJson as parseJson
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
		
		#empty generated dirs
		indexDir = 'indexes'
		if os.path.isdir(indexDir):
			shutil.rmtree(indexDir)
		os.mkdir(indexDir)

		cssDir = 'static/css'
		if os.path.isdir(cssDir):
			shutil.rmtree(cssDir)
		os.mkdir(cssDir)

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

		folder = 'static/requireJs'
		for the_file in os.listdir(folder):
			file_path = os.path.join(folder, the_file)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
			except Exception, e:
				print e
		
		self.globalInc = globalInc.init()

		self.externalJsInc = []
		self.globals = {}
		self.globals['js'] = copy.copy(self.globalInc.jsInc)
		self.globals['css'] = copy.copy(self.globalInc.cssInc)
		self.globals['htmlTemplates'] = copy.copy(self.globalInc.templates)

		globalJsInc = 'static/requireJs/global.js'
		jsFile = open(globalJsInc, 'w+')
		jsFile.write(self.renderJS(self.globals['js'], self.globals['htmlTemplates']))

		mainCssInc = 'static/css/global.css'
		cssFile = open(mainCssInc, 'w+')
		cssFile.write(self.renderCSS(self.globals['css']))

		#loop over each profile
		for profile in self.profiles:
			#set the current profile
			self.profile = profile
			
			#init the config based on current profile
			self.config = configPages.init(self.profile)

			#loop over each page listed in config
			for page in self.pages:
				#apply global config
				self.baseTemplate = copy.copy(self.config.baseTemplate)
				
				self.js = []
				for jsInc in self.globals['js']:
					if not isinstance(jsInc, dict):
						self.js.append(jsInc)

				self.js.extend(copy.copy(self.config.jsInc))
			
				self.css = []
				for cssInc in self.globals['css']:
					if not isinstance(cssInc, dict):
						self.css.append(cssInc)

				#self.css.extend(copy.copy(self.config.cssInc))
				self.htmlTemplates = []
				
				
				self.views = copy.copy(self.config.views)
				
				self.head = {
					'title' : 'Where should i store the default title?'
				}
				
				self.pageTemplate = '{{{content}}}'
				
				#import current page config
				pageConfigString = open('pages/home/config.json')
				pageConfigJson = json.load(pageConfigString)
				pageConfigString.close()
				
				
				
				pageConfig = __import__('pages.' + page + '.config', fromlist=['config'])
				
				#print pageConfig
				
				pageConfigJson = pageConfig.init(profile)
				
				#print 'configJson'
				#print pageConfigJson.jsInc
				
				#apply page config
				self.applyPageConfig(pageConfigJson, self)
	
				#apply view configs
				if self.views:
					for view in self.views:
						self.applyViewConfigs(self.views[view], self)
				
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
				curr.applyViewConfigs(pageConfig.views[nestedView], curr)

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
				curr.applyViewConfigs(viewConfig.views[nestedView], curr)

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

		orderedExtJsInc = []
		for externalJs in externalJsInc:
			if externalJs['url'][0] != '/':
				orderedExtJsInc.append(externalJs)

		return orderedExtJsInc

	#compiles local css
	def renderCSS(self, cssFiles):
		cssInc = ''
		for cssFile in cssFiles:
			if isinstance(cssFile, dict):
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
		profilePage = profile + '-' + pageName		

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
