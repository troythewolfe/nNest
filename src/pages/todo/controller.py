from util.controllerPage import Page
import os

def init(profile):
	page = Page(profile, os.path.abspath(__file__))
	return page.render('nav content')
