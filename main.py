import params as cfg
#from modem import modem
from datastore import store as ds
import logging
import time
import datetime
from multiprocessing import Process, Pipe

logging.basicConfig(filename='liter.log', encoding='utf-8', level=logging.DEBUG)

# setting up datastore
ds.uri = cfg.store_path
db = ds.db
def prepare():
    logging.debug('Starting services %s'% datetime.datetime.now())
def finish():
    pass
def run():
    RUN = True
    while RUN:
        logging.debug('loop round')
        time.sleep(cfg.sleep_time)

if __name__ == "__main__":
    # starting services
    prepare()
    # execute only if run as a script
    run()
