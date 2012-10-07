from flask import Flask, request
import appSettings.pageRouter as pageRouter

#create flask app object
app = Flask(__name__, static_path='/static')

#pass app object to page router
pageRouter.init(app, request)

if __name__ == '__main__':
    app.run()
