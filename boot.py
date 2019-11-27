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

ssid = 'Fios-Y20XF'
password = 'glad3577age0826car'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

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