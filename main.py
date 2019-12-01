import uasyncio as asyncio
import utime

async def bar():
    count = 0
    while True:
        count += 1
        print(count)
        await asyncio.sleep(1)  # Pause 1s

async def foo():

    print("DRAIN")    
    await asyncio.sleep(2)
    print("FILL WATER")
    await asyncio.sleep(2)
    print("FILL CLEANER")
    await asyncio.sleep(2)
    print("DRAIN")
    await asyncio.sleep(2)
    while True:
        print("Bob")
        await asyncio.sleep(2.6)

def web_page():
  print("starting web_page()")
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

print("starting web_server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
s.setblocking(1)
s.settimeout(.1)

async def web_server():
    print("STARTING web server")
    while True:
        print(utime.time())
        # await asyncio.sleep(6)
        try:
            conn, addr = s.accept()
            print("past accept")
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            print("After .recv")
            print(str(request))
            request = str(request)
            print("A")
            start_on = request.find('/?start=on')
            start_off = request.find('/?start=off')
            if start_on == 6:
                print('START ON')
            if start_off == 6:
                print('START OFF')
            print("C")
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()      

        except:
            print("FALSE")
            await asyncio.sleep(1)

        print(utime.time()) 

loop = asyncio.get_event_loop()
loop.create_task(bar()) # Schedule ASAP
loop.create_task(foo())
loop.create_task(web_server())
loop.run_forever()
