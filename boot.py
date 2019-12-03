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

# for connecting to local wifi network
# with open('credentials.json', 'r') as credentials:
#   data = json.load(credentials)
#   ssid = data['ssid']
#   password = data['password']
# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.connect(ssid, password)
# while station.isconnected() == False:
#   pass

# for using as access point
ssid = 'keg-washer'
password = 'keg-washer'
station = network.WLAN(network.AP_IF)
station.active(True)
station.config(essid=ssid, password=password)
while station.active() == False:
  pass

print('Connection successful')
print(station.ifconfig())

relay = Pin(16, Pin.OUT)
relay.off()

co2 = Pin(2, Pin.OUT)
lp_water = Pin(4, Pin.OUT)
hp_water = Pin(5, Pin.OUT)
lp_cleaner = Pin(12, Pin.OUT)
hp_cleaner = Pin(13, Pin.OUT)
lp_santizer = Pin(14, Pin.OUT)
hp_santizer = Pin(15, Pin.OUT)

def all_off():
    co2.off()
    lp_water.off()
    hp_water.off()
    lp_cleaner.off()
    hp_cleaner.off()
    lp_santizer.off()
    hp_santizer.off()

all_off()    

profile_file = open('profile.json', 'r')
profile = json.load(profile_file)
