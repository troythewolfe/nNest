#build.py

Run `python build.py` to crawl root, page and view configs.

Generates:

- Index templates in `/src/indexes/`
- Concatinated and minified css files into `/src/static/css/`
- Concatinated and minified js files into `/src/static/js/`

Generated files follow the naming convention `<profile>-<page>.ext`

#server.py

Run `python server.py` to start listening on port `5000`

Currently, you set these two variables here:
 
- `SERVER_NAME = '127.0.0.1'`
- `SERVER_PORT = 5000`