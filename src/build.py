import inc
import config
import pystache
import copy
import util.profileParser
import profileList
import shutil
import os
import sys
sys.path.append('/')

class Build():
	def __init__(self):
		#empty generated dirs
		shutil.rmtree('indexes')
		os.mkdir('indexes')

		shutil.rmtree('static/js')
		os.mkdir('static/js')

		shutil.rmtree('static/css')
		os.mkdir('static/css')

		#get registered profiles
		self.profiles = profileList.init()

		#loop over each profile
		for profile in self.profiles:
			#set the current profile
			self.profile = profile

			#init the config based on current profile
			self.config = config.init(self.profile)

			#loop over each page listed in config
			for pageConfig in self.config['pages']:
				#apply global config
				self.baseTemplate = copy.copy(self.config['baseTemplate'])
				self.js = copy.copy(self.config['jsInc'])
				self.css = copy.copy(self.config['cssInc'])
				self.views = copy.copy(self.config['views'])
				self.titleTag = copy.copy(self.config['titleTag'])
				self.pageTemplate = '{{{content}}}'
				
				#apply page config
				self.applyPageConfig(self.config['pages'][pageConfig])
	
				#apply view configs
				if self.views:
					for view in self.views:
						self.applyViewConfigs(self.views[view])
				
				#render page
				self.render(self.pageTemplate, self.pageName, self.profile)
	
	#overwrite defaults and add page specific configs
	def applyPageConfig(self, pageConfig):		
		if 'titleTag' in pageConfig:
			self.titleTag = pageConfig['titleTag']
	
		if 'baseTemplate' in pageConfig:
			self.baseTemplate = pageConfig['baseTemplate']
		
		if 'jsInc' in pageConfig:
			self.js.extend(pageConfig['jsInc'])
		
		if 'cssInc' in pageConfig:
			self.css.extend(pageConfig['cssInc'])
		
		if 'pageTemplate' in pageConfig:
			self.pageTemplate = pageConfig['pageTemplate']

		if 'pageName' in pageConfig:
			self.pageName = pageConfig['pageName']
		
		#print self.config['pages'][pageConfig]

	def applyViewConfigs(self, views):
		#if 'jsInc' in views['']:
		#print views
		return False

	#compiles local js
	def renderJS(self):
		jsInc = ''
		externalJsInc = []
		for jsFile in self.js:
			if isinstance(jsFile, dict):
				jsInc += jsFile['source'] + '\n'
	
		return jsInc

	#puts all external js files into an object
	def getJS(self):
		externalJsInc = []
		for jsFile in self.js:
			if not isinstance(jsFile, dict):
				externalJsInc.append({ 'url' : jsFile })
	
		return externalJsInc

	def renderCSS(self):
		cssInc = ''
		for cssFile in self.css:
			if isinstance(cssFile, dict):
				cssInc += cssFile['source'] + '\n'
	
		return cssInc

	#puts all external js files into an object
	def getCSS(self):
		externalCssInc = []
		for cssFile in self.css:
			if not isinstance(cssFile, dict):
				externalCssInc.append({ 'url' : cssFile })
	
		return externalCssInc
	
	#render index
	def render(self, content, pageName, profile):
		#add generated js/css files to lists
		profilePage = profile + '-' + pageName		

		mainJsInc = 'static/js/' + profilePage + '-min.js'
		jsFile = open(mainJsInc, 'w+')
		jsFile.write(self.renderJS())
		self.js.append('/' + mainJsInc)

		mainCssInc = 'static/css/' + profilePage + '-min.css'
		cssFile = open(mainCssInc, 'w+')
		cssFile.write(self.renderCSS())
		self.css.append('/' + mainCssInc)

		#assing template variables
		templateContent = {
			'title' : self.titleTag,
			'jsInc' : self.getJS(),
			'cssInc' : self.getCSS(),
			'bodyContent' : content
		}

		#create index file
		indexFile = open('indexes/' + profilePage + '.html', 'w+')
		pageTemplate = inc.html(self.baseTemplate)
		indexFile.write(pystache.render(pageTemplate['source'], templateContent))

build = Build()