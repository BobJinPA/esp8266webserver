import uasyncio as asyncio
import utime

clean_state = False

async def sleep(seconds):
    for i in range(seconds * 10):
        if (clean_state):
            await asyncio.sleep(.1)
        else:
            return False
    return True

def interface(step):
    if step == "co2":
        return co2
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
    for step_set in profile:
        all_off()
        for step in step_set["steps"]:
            print(step)
            interface(step).on()
        await sleep(step_set["duration"])


async def clean():
    global clean_state
    while True:
        if clean_state:
            await clean_process()
            all_off()
            print("CLEANER DONE")
            clean_state = False
        else:
            all_off()
            await asyncio.sleep(.2)

def web_page():
    if clean_state == True:
      cleaner_state="ON"
    else:
      cleaner_state="OFF"
    
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
    <h1>Keg Cleaner</h1> 
    <p>Cleaner state: <strong>""" + cleaner_state + """</strong></p>
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
                print('START CLEANER')
                clean_state = True
            if start_off == 6:
                print('STOP CLEANER')
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
loop.create_task(clean())
loop.create_task(web_server())
loop.run_forever()
