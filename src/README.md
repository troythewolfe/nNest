#build.py

Runs in `server.py` and crawl root, page and view configs.

Must

Generates:

- Index templates in `/src/indexes/`
- Global js and css files into `/src/static/`
- Concatinated and minified profile-page css files into `/src/static/css/`
- Concatinated and minified profile-page js files into `/src/static/js/`

Generated files follow the naming convention `<profile>-<page>.ext`

#server.py

Run `python server.py` to start listening on port `5000`

Currently, you set these two variables here:
 
- `SERVER_NAME = '127.0.0.1'`
- `SERVER_PORT = 5000`
