from ua_parser import user_agent_parser
import util.profileParser as profileParser

def init(app, request):
	#app pages
	@app.route('/')
	def home():
		import pages.home.controller as page
		return processPage(page)

	@app.route('/calendar/')
	def calendar():
		import pages.calendar.controller as page
		return processPage(page)
		
	@app.route('/calendar/<year>/<month>/<day>/')
	def calendarDate(year, month, day):
		import pages.calendar.controller as page
		return processPage(page, {
			'year' : year,
			'month' : month,
			'day' : day
		})
	
	@app.route('/todo/')
	def todo():
		import pages.todo.controller as page
		return processPage(page)
	
	#system pages
	@app.errorhandler(404)
	def error404(error):
		return 'page not found'

	#helpers
	def processPage(page, pathParams={}):
		return page.init(profileParser.init(request, pathParams))