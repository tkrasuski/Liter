# This is Liter Web Client and Connectivity Application Server 
# Server provides web gui and connectivity with other Liter servers via REST API

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import base64 as b64

db = None

class Index(RequestHandler):
    def get(self):
        if db:
            res = db(db.ltopic.id>0).count()
            self.write({'message': res})
        else:
            self.write({'message':'no db'})
class API_topic(RequestHandler):
    def get(self):
        pass
    def post(self):
        pass
class API_resource(RequestHandler):
    def get(self):
        pass
    def post(self):
        pass

def make_app():
    urls=[
        ("/", Index),
        ("/api/topic",API_topic),
        ("/api/resource",API_resource)]
    return Application(urls)

def run():
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
