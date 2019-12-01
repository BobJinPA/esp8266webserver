import uasyncio as asyncio
import utime

clean_state = False

async def counter():
    count = 0
    while True:
        count += 1
        print("--", str(count))
        await asyncio.sleep(1)  # Pause 1s


async def sleep(seconds):
    for i in range(seconds):
        if (clean_state):
            await asyncio.sleep(1)
        else:
            return False
    return True


def interface(step):
    if step == "drain":
        return drain
    if step == "fill low pressure water":
        return lp_water
    if step == "fill high pressure water":
        return hp_water
    if step == "fill low pressure cleaner":
        return lp_cleaner
    if step == "fill high pressure cleaner":
        return hp_cleaner
    if step == "fill low pressure sanitizer":
        return lp_santizer
    if step == "fill high pressure sanitizer":
        return hp_santizer   
    return False


async def clean_process():
    for item in profile:
        all_off()
        print(item["step"])
        interface(item["step"]).on()
        await sleep(item["duration"])


async def clean():
    global clean_state
    while True:
        # print("Test state", str(clean_state))
        if clean_state:
            await clean_process()
            clean_state = False
        else:
            await asyncio.sleep(.2)

def web_page():
    if drain.value() == 1:
      gpio_state="ON"
    else:
      gpio_state="OFF"
    
    html = """<html>
    <head>
    <title>Keg Cleaner</title>
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
    <p>Cleaner state: <strong>""" + gpio_state + """</strong></p>
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
s.setblocking(1)
s.settimeout(.2)

async def web_server():
    global clean_state
    while True:
        try:
            conn, addr = s.accept()
            print('Got a connection from %s' % str(addr))
            request = conn.recv(1024)
            request = str(request)
            start_on = request.find('/?start=on')
            start_off = request.find('/?start=off')
            if start_on == 6:
                print('START ON')
                clean_state = True
            if start_off == 6:
                print('START OFF')
                clean_state = False
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()      

        except:
            await asyncio.sleep(.2)


loop = asyncio.get_event_loop()
# loop.create_task(counter())
loop.create_task(clean())
loop.create_task(web_server())
loop.run_forever()
