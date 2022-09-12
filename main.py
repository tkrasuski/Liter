import params as cfg
#from modem import modem
from datastore import store as ds
import logging
import time
import datetime
from multiprocessing import Process, Pipe
from web import server

logging.basicConfig(filename='liter.log', encoding='utf-8', level=logging.DEBUG)

# setting up datastore
ds.uri = cfg.store_path
db = ds.db
def prepare():
    logging.debug('Starting services %s'% datetime.datetime.now())
    server.db = db
    p = Process(target=server.run(), args=())


def finish():
    pass
def run():
    RUN = True
    while RUN:
        logging.debug('Main loop round %s')
        time.sleep(cfg.sleep_time)

if __name__ == "__main__":
    # starting services
    prepare()
    # execute only if run as a script
    run()
### https://docs.python.org/3/library/multiprocessing.html