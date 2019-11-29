# import web

# Complete project details at https://RandomNerdTutorials.com
import time

def web_page():
  if drain.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html>
  <head>
  <title>ESP Web Server</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> 
  <style>
  html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
  .button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}
  </style>
  </head>
  <body> 
  <h1>Keg Cleaner Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
  <p>
  <a href="/?start=on">
  <button class="button">START</button>
  </a>
  </p>
  <p>
  <a href="/?start=off"><button class="button button2">STOP</button></a>
  </p>
  </body>
  </html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


def all_off():
  drain.off()
  lp_water.off()
  hp_water.off()
  lp_cleaner.off()
  hp_cleaner.off()
  lp_santizer.off()
  hp_santizer.off()

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  start_on = request.find('/?start=on')
  start_off = request.find('/?start=off')
  if start_on == 6:
    print('START ON')
    all_off()
    drain.on()
    time.sleep(1)
    all_off()
    lp_water.on()
    time.sleep(1)
    all_off()
    hp_water.on()
    time.sleep(1)
    all_off()
    drain.on()
    time.sleep(1)
    all_off()
    hp_water.on()
    time.sleep(1)
    all_off()
    lp_cleaner.on()
    time.sleep(1)
    all_off()
    hp_cleaner.on()
    time.sleep(1)
    all_off()
    drain.on()
    lp_water.on()
    time.sleep(1)
    all_off()
    hp_water.on()
    time.sleep(1)
    all_off()
    drain.on()
    time.sleep(1)
    lp_santizer.on()
    time.sleep(1)
    all_off()
    hp_santizer.on()
    time.sleep(1)
    all_off()
    drain.on()
    time.sleep(1)
    all_off()
    lp_water.on()
    time.sleep(1)
    all_off()
    hp_water.on()
    time.sleep(1)
    all_off()
    drain.on()

  if start_off == 6:
    print('START OFF')
    all_off()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()