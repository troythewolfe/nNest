from flask import Flask, request
import appSettings.router as router
import appSettings.profileParser as profileParser

#create flask app object
app = Flask(__name__, static_path='/static')

#helpers
def processPage(page, pathParams={}):
	return page.init(profileParser.init(request, pathParams))

#pass app object to page router
router.init(app, request, processPage)

if __name__ == '__main__':
    app.run()
