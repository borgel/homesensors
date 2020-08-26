'''
assume that boot.py has connected us to the network already.
'''
import time
import json
import sys
import aqi

#import requests or urequests
try:
   print("On target")
   import urequests as requests
   from machine import Pin
   import machine

   # init i2c for the servo controller
   i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

   import pca9685
   import servo
except ImportError:
   print("On host?")
   import requests

SENSOR_URL = "https://www.purpleair.com/json?show=19855"
LOOP_DELAY_S = 2 * 60

s = servo.Servos(i2c)

# we don't need the soft AP
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

# onboard LED. on/off reversed
led = Pin(2, Pin.OUT)

while True:
   # if the network connection is down, reboot and let the boot.py try to reconnect us
   if not sta_if.isconnected():
      print("Not connected to network, rebooting")
      time.sleep(0.5)
      machine.reset()

   led.value(not led.value())

   gc.collect()
   # FIXME rm
   print("Top...");

   sensor_raw = requests.get(SENSOR_URL)
   if sensor_raw.status_code != 200:
      print("Failed to get sensor value: code {}".format(sensor_raw.status_code))
      time.sleep(LOOP_DELAY_S)
      continue
   sensor = sensor_raw.json()

   print(sensor)

   # get the current stats object (for some reason it's a JSON object embedded in a string)
   stats = json.loads(sensor['results'][0]['Stats'])
   # the 10 minute average (the shortest non-instant reading)
   avg = aqi.aqi_from_pm(stats['v1'])

   # make it something we can servo, assuming our max range goes up to 200 counts
   percentage = avg / 200.0
   deg = 180 - (percentage * 180.0)

   print("Currently {}% badness ({} degrees)".format(100 * percentage, deg))

   # now, do a servo!
   s.position(0, degrees=deg)

   time.sleep(LOOP_DELAY_S)

