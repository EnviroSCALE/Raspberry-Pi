import time
from my_libs import *
import heapq;
import random;
import Queue;
import json

setup_logging()
log = logging.getLogger("<Sensor>")


class Callable():
    def call(sim):
        raise Exception('Call of %s is not implemented' % self)

class Sensor(Callable):

    def __init__(self, name, readlatency, period, size, gamma):
        """
        Construct a new 'Sensor' object.
        :param name: The name of Sensor
        :param readlatency: read latency
        :param period: The period to read
        :param size: The size of sensor reading in bytes
        :return: returns nothing
        """
        self.name = name
        self.readlatency = readlatency
        self.period = period
        self.size = size
        self.gamma = gamma
        self.flag = False

    def __repr__(self):
        return 'Sensor::%s' % self.name

    def set_period(self, period):
        self.period = period

    def call(self, sim):
        if self.flag:
            self.flag = False
            print 'Time %f sensor %s reading completed' % (sim.simclock, self)
            sim.add_event(sim.simclock + self.period, self)
        else:
            self.flag = True
            sim.read_queue = sim.read_queue + self.size
            reading = Reading(self.name, sim.simclock, self.size)
            sim.readings_queue.put(reading)
            print 'Time %f reading sensor %s current queue %d' % (sim.simclock, self, sim.read_queue)
            sim.add_event(sim.simclock + self.readlatency, self)



class Reading:
    def __init__(self, sensor_name, sensing_time, size):
        self.sensor_name = sensor_name
        self.sensing_time = sensing_time
        self.size = size

    def __repr__(self):
        return 'Sensor::%s' % self.sensor_name