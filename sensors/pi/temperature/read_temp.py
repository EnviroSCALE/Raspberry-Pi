import time
import datetime
from Sensor import Sensor
from my_libs import *
import random

setup_logging()
log = logging.getLogger("DHT11Exception")

class Temperature(Sensor):
    def __init__(self, digital):
        self.device_name="DHT11"
        self.digital = digital
        self.interval = 2  # initialize GPIO
        self.verbose = False

    def read(self):
        try:
            return random.randint(26, 28),  random.randint(44, 46)
        except:
            eprint("ERROR in READ...PI/sensors/temperature/read_temp.py")
            log.exception("ERROR in READ...PI/sensors/temperature/read_temp.py")
