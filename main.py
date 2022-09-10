import params as cfg
#from modem import modem
from datastore import store as ds
import logging
import time
logging.basicConfig(filename='liter.log', encoding='utf-8', level=logging.DEBUG)

def run():
    RUN = True
    while RUN:
        logging.debug('loop round')
        time.sleep(cfg.sleep_time)

if __name__ == "__main__":
    # execute only if run as a script
    run()