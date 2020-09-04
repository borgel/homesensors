import uos, machine
import gc

import network
import time

gc.collect()

# TODO replace these
ssid = "YOURNETWORK"
psk = "YOURPASSWORD"

# connect to wifi
attempts_remain = 10
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
   print('connecting to network...')
   sta_if.active(False)
   time.sleep(1)
   sta_if.active(True)
   sta_if.connect(ssid, psk)
   while not sta_if.isconnected() and attempts_remain > 0:
      attempts_remain = attempts_remain - 1
      time.sleep(1)

print('Network config:', sta_if.ifconfig())

