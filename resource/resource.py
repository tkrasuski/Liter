## 
import hashlib
import random
import datetime
import codecs

def new_rid():
    random.randint(1, 1000)
    date = datetime.datetime.now()
    #print(str(date)+str(random))
    hash_ = hashlib.md5(bytes(str(date)+str(random),encoding='utf-8'))
    return hash_.hexdigest()

class Topics(object):
    def __init__(self,db):
        self.db=db
        self.rid=None
        self.topic_name=None
        self.description = None
    def get_list(self):
        qry = self.bd(self.db.ltopic.id>0).select()
        return qry
    def get_by_id(self, lid):
        qry = self.db(self.db.ltopic.id==lid)
        return qry
    def new(self):
        self.db.ltopic.insert(rid=new_rid(), topic_name=self.topic_name, description=self.description)
        self.db.commit()
class Resource(object):
    def __init__(self, db):
        self.db = db
        self.id = None
        self.rtype = None # must be one of TEXT, BINARY, MD, HTML
        self.ext = None # if rtype is BINARY this field should contain file extension
        self.created_by = None
    def get_by_id(self,id):
        pass
