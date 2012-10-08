def init(app, processPage):
	#app pages
	@app.route('/')
	def home():
		import pages.home.controller as page
		return processPage(page)

	@app.route('/calendar/')
	def calendar():
		print 'cal1'
		import pages.calendar.controller as page
		print 'cal12'
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
		print 'before todo'
		import pages.todo.controller as page
		print 'after todo'
		return processPage(page)
	
	#system pages
	@app.errorhandler(404)
	def error404(error):
		return 'page not found'