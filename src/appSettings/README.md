#config.py

###Requires

	import util.inc as inc
	from util.configRoot import ConfigRoot

Build time config that extends `util.configRoot`.

`init [Function]` build-time

###Parameters

- `profile [String]` Accepts the current profile, as determined by `build.py`

###Returns

`profile [Class] extends ConfigRoot`

###Usage

Within the init, you create an instance of the `ConfigRoot` class, assign values to its properties, then return it.

	def init(profile):
		config = ConfigRoot()
	
		#import pages
		import pages.home.config as home
		import pages.calendar.config as calendar
		import pages.todo.config as todo
		
		config.pages = {
			'home' : home.init(profile),
			'calendar' : calendar.init(profile),
			'todo' : todo.init(profile)	
		}
		
		return config

#profileList.py

This list tells `build.py` what profile assets to build. 

`init [Function]` build-time

	profiles = [
		'modernWeb',
		'legacyWeb',
		'chromeWeb'
	]

###Returns

`[List][String]` representing the profile names.

#profileParser.py

`init [Function]` run-time

###Parameters

- `ua [Dict]` Parsed user agent object 
- `request [Dict]` The flask request object 
- `pathParams [Dict] Optional` Path parameters determined in router.py

###Returns

`[String]` of the current profile name.

#router.py

`init [Function]` run-time

###Parameters

- `app [Dict]` The flask app object, used to create routes
- `processPage [Function]` A function that ultimately returns a built `String` of the HTML output, defined and passed in from `server.py`

###Usage

Within the init function, routes are defined:
	
	# define the path
	@app.route('/') 
	# create a function
	def home():
		# import the page that this route wants
		import pages.home.controller as page
		# process the imported page
		return processPage(page)

To define a route with parameters:
	
	# section in the path definition within <> 
	# become available as parameters within the function
	@app.route('/calendar/<year>/<month>/<day>/')
	def calendarDate(year, month, day):
		import pages.calendar.controller as page
		
		# processPage will accept an optional second paramter of the path parameters
		return processPage(page, {
			'year' : year,
			'month' : month,
			'day' : day
		})
	
