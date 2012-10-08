#configRoot.py

`ConfigRoot` [Class]

###Properties

- `pages [Dict]` 
	- `key [String]` pageName (same as src/pages/pageName/)
	- `value [Class]` `Page` extension of `controllerPage`
- `views[Dict]` 
	- `key [String]` viewName (same as src/views/viewName/)
	- `value [Class]` View extension of controllerView
- `head [Dict]`
	- `title [String]` The contents of the HTML `<title>` tag
- `baseTemplate [String]` The templateName in `/src/html/templateName.html` without the extension.  Example: `'base'` instead of `'base.html'`
- `jsInc [List][String || Dict]`
	- If entry is of type `String` it is treated as a file that lives on a different server, and is included in the page within its own `<script>` tag
	- If entry is of type 'Dict'
		- location [String] The file location. Example: `/src/pages/pageName/js/fileName.js`
		- source [String] The contents of the file
- `cssInc [List][String || Dict]`
	- If entry is of type `String` it is treated as a file that lives on a different server, and is included in the page within its own `<link>` tag
	- If entry is of type 'Dict'
		- `location [String]` The file location. Example: `/src/pages/pageName/css/fileName.js`
		- `source [String]` The contents of the file
		
	

#configPage.py

`ConfigPage` [Class]

###Requires

	import util.inc as inc
	import os

###Parameters:

- `loc [Object]` Passed in as `os.path.abspath(__file__)`, to get name of parent directory

###Properties:

- `name [String]` pageName of the directory within `/src/pages/nageName`.  Based on `loc` parameter. 
- html [Dict] 
	- `location [String]` The location of the HTML file. Example: `/src/pages/pageName/html/fileName.html`.
	- `source [String]` The content of the file
- `head [Dict]`
	- `title [String]` The contents of the HTML `<title>` tag
- `views[Dict]` 
	- `key [String]` viewName (same as src/views/viewName/)
	- `value [Class]` View extension of controllerView
- `jsInc [List][String || Dict]`
	- If entry is of type `String` it is treated as a file that lives on a different server, and is included in the page within its own `<script>` tag
	- If entry is of type 'Dict'
		- `location [String]` The file location. Example: `/src/pages/pageName/js/fileName.js`
		- source [String] The contents of the file
- `cssInc [List][String || Dict]`
	- If entry is of type `String` it is treated as a file that lives on a different server, and is included in the page within its own `<link>` tag
	- If entry is of type 'Dict'
		- `location [String]` The file location. Example: `/src/pages/pageName/css/fileName.js`
		- `source [String]` The contents of the file

###Methods:

`set [Function]` Sets `html`, `js` and `css` files as class property values.

####Parameters:

- `ext [String]` The type of property you want to set. Example `'html'` or `'js'`
- `name [String] optional, default=False` The name of the file to set. If it is not set, it looks for a file with same name as the page.


#configView.py

##TODO

#controllerPage.py

`ConfigPage` [Class]

###Requires

	import util.inc as inc
	import pystache
	import os

###Parameters:

- `profile [Dict]` The profile object as defined in `server.py` 
- `loc [Object]` Passed in as `os.path.abspath(__file__)`, to get name of parent directory

###Properties:
- `profile [Dict]` Set to `self.profile` based on the `profile` parameter
- `name [String]` The name of the parent directory, based `loc` parameter

###Methods:

`render [Function]`

####Parameters:

`content [Dict || String]` 

- If `[Dict]` It will assume it corresponds to the template tags within the page index, populate it and return it as a string.  
- if `[String]` It will return the string only.

#controllerView.py

#inc.py





