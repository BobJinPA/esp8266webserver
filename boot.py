# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import json
with open('credentials.json') as credentials:
  data = json.load(credentials)
  ssid = data['ssid']
  password = data['password']

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

<<<<<<< HEAD
relay = Pin(16, Pin.OUT)
relay.off()

drain = Pin(2, Pin.OUT)
lp_water = Pin(4, Pin.OUT)
hp_water = Pin(5, Pin.OUT)
lp_cleaner = Pin(12, Pin.OUT)
hp_cleaner = Pin(13, Pin.OUT)
lp_santizer = Pin(14, Pin.OUT)
hp_santizer = Pin(15, Pin.OUT)
=======
# # led = Pin(2, Pin.OUT)

# # This file is executed on every boot (including wake-boot from deepsleep)
# #import esp
# #esp.osdebug(None)
# import uos, machine
# #uos.dupterm(None, 1) # disable REPL on UART(0)
# import gc
# #import webrepl
# #webrepl.start()
# gc.collect()

# import time

# led = Pin(2, Pin.OUT)
led.on()
time.sleep(1)
led.off()
time.sleep(1)
led.on()
>>>>>>> f6d463bd7b36b02ef4b64c794e47cfa840c84053
