import network
import web
import uasyncio as asyncio
from wificonf import wifiConf

# access point credentials
#AP_SSID = 'WebSocket AP'
#AP_PASSWORD = 'donthackmebro'
#AP_AUTHMODE = network.AUTH_WPA_WPA2_PSK

# print("Create WiFi access point")
# wlan = network.WLAN(network.AP_IF)
# wlan.active(True)
# wlan.config(essid=AP_SSID, password=AP_PASSWORD, authmode=AP_AUTHMODE)
# while wlan.active() == False:
#     pass
# print(wlan.ifconfig())

async def startWifi(pubsub):
    ssid, key = wifiConf
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, key)
    while not wlan.isconnected():
        pass
    
    print(wlan.ifconfig())

    app = web.App(host='0.0.0.0', port=80)
    
    # root route handler
    @app.route('/')
    async def index_handler(r, w):
        w.write(b'HTTP/1.0 200 OK\r\n')
        w.write(b'Content-Type: text/html; charset=utf-8\r\n')
        w.write(b'\r\n')
                    
        with open('index.html', encoding='utf8') as f:
            for line in f:
                w.write(line.strip())

        await w.drain()

    # Store current WebSocket clients
    WS_CLIENTS = set()

    # /ws WebSocket route handler
    @app.route('/ws')
    async def ws_handler(r, w):
        # upgrade connection to WebSocket
        ws = await web.WebSocket.upgrade(r, w)
        r.closed = False
        # add current client to set
        WS_CLIENTS.add(ws)
        while ws.open:
            # handle ws events
            evt = await ws.recv()
            if evt is None or evt['type'] == 'close':
                ws.open = False
            elif evt['type'] == 'text':
                pubsub.publish('web', evt['data'])
                # echo received message to all clients
                for ws_client in WS_CLIENTS:
                    try:
                        await ws_client.send(evt['data'])
                    except:
                        continue
        # remove current client from set
        WS_CLIENTS.discard(ws)
    
    await app.serve()
    
    