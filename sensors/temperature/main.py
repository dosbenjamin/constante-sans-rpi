from utils.socketio_client import *
import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT11_pin = 24

@sio.event
def temperature_state(value):
  sio.emit('temperature_state', value)
