# This is Liter Web Client and Connectivity Application Server 
# Server provides web gui and connectivity with other Liter servers via REST API

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import base64 as b64
import random
import datetime
import hashlib
import json as js
db = None

def new_rid():
    random.randint(1, 1000)
    date = datetime.datetime.now()
    #print(str(date)+str(random))
    hash_ = hashlib.md5(bytes(str(date)+str(random),encoding='utf-8'))
    return hash_.hexdigest()


class Index(RequestHandler):
    def get(self):
        if db:
            res = db(db.ltopic.id>0).count()
            self.write({'message': res})
        else:
            self.write({'message':'no db'})
class API_welcome(RequestHandler):
    ''' This class returns new session for incoming connection
        session id is used to identify server 
    '''
    def get(self):
        cnt=[]
        rows = db(db.lsession.id>0).select()
        for r in rows:
            cnt.append({'lcall':r.lcall, 'lsid':r.lsid, 'stamp':r.stamp.strftime("%m/%d/%Y, %H:%M:%S")})
            #print(r)
        self.write({'message': cnt})
    def post(self):
        row = js.loads(self.request.body.decode('utf-8'))
        #print (type(row))
        if 'call' in row:
            # remove any prevoious sessions
            db(db.lsession.lcall==row['call']).delete()
            # create session
            sid = new_rid()
            db.lsession.insert(lcall=row['call'],lsid=sid)
            db.commit()
            self.write({'sid':sid})
        else:
            self.write({'message': 'Invalid request'})
class API_topic(RequestHandler):
    def get(self,param):
        '''
        param can be:
        LA - listing all topics with ids
        GN - get id by name or returns 404
        ID= - get all topic data by suplied ID
        '''
        if param == 'LA':
            message = []
            rows = db(db.ltopic.id>0).select()
            for r in rows:
                message.append(dict(id=r.rid, topic_name=r.topic_name, description=r.description))
            self.write(dict(message=message))

        elif param[0:2] == 'GN':
            pass
        elif param[0:3] == 'ID=':
            message=[]
            id = param[3:]
            r= db(db.ltopic.rid==id).select().first()
            message.append(dict(id=r.rid, topic_name=r.topic_name, description=r.description))
            self.write(dict(message=message))

        else:
            raise tornado.web.HTTPError(400)
    def post(self):
        message='OK'
        row = js.loads(self.request.body.decode('utf-8'))
        if 'sid' in row:
            sid = row['sid']
        # checking if session is registered
            il = db(db.session.lsid==sid).count()
            if il>0:
                db.ltopic.insert(rid=new_rid(),topic_name=row['topic_name'], description=row['description'])
        else:
            message = 'No session id'
            self.write(dict(message=message))


class API_resource(RequestHandler):
    def get(self):
        pass
    def post(self):
        pass

def make_app():
    urls=[
        ("/", Index),
        ("/api/welcome",API_welcome),
        ("/api/topic/([^/]+)",API_topic),
        ("/api/resource/([^/]+)",API_resource)]
    return Application(urls, debug=True)

def run():
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
