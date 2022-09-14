from gluon import *
from pydal import DAL, Field
from pydal import validators as v
import datetime as dt
uri = 'sqlite://data/storage.sqlite'

db = DAL(uri, pool_size=10, migrate_enabled=True,check_reserved=['all'])
db.define_table('ltopic',
                Field('rid','string'),
                Field('topic_name','string'),
                Field('description','text'),
                Field('stamp','datetime', default=dt.datetime.now())
                )
db.define_table('lresource',
                Field('rid','string'),
                Field('source_call','string'),
                Field('resource_name','string'),
                Field('topic',requires=v.IS_IN_DB(db, 'ltopic.rid', '%(name)s')),
                Field('stamp','datetime', default=dt.datetime.now())
                )
db.define_table('lmessage',
                Field('rid','string'),
                Field('subject','string'),
                Field('from_call','string'),
                Field('to_call','string'),
                Field('msg_content','text'),
                Field('creation_date','datetime'),
                Field('arrival_date','datetime'),
                Field('lpath','text'),
                Field('stamp','datetime', default=dt.datetime.now())
                )
db.define_table('lrouter',
                Field('area','string'),
                Field('via_call','string'),
                Field('to_call','string'),
                Field('rstate','string',requires=v.IS_IN_SET(('A','N'))),
                Field('stamp','datetime', default=dt.datetime.now())
                )
db.define_table('lsession',
                Field('lcall','string'),
                Field('lsid','string'),
                Field('stamp','datetime', default=dt.datetime.now())
                )