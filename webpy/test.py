import web
import json
# for using templates:
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/index.json', 'index_json'
)

class index:
    def GET(self):
        return render.index()

class index_json:
    def GET(self):
      #get the json (could be from a file or just json right here)
      #jsonData = {'one':1,'two':2}
      with open('json/index.json') as json_file:
        jsonData = json.load(json_file)

      #set headers
      web.header('Content-Type', 'application/json')

      #render json
      return json.dumps(jsonData)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
