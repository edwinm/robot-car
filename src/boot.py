# boot.py -- run on boot-up

from machine import Pin, PWM
import uasyncio as asyncio

from motor import Motor
from wifi import startWifi
from pubsub import PubSub

pubsub = PubSub()

motor = Motor(2, 3, 4, 7, 5, 6)

def handleWeb(data):
    if data == 'left':
        motor.move(0, 50)
    elif data == 'right':
        motor.move(50, 0)
    elif data == 'stop':
        motor.move(0, 0)
            
async def runMotor():
    await asyncio.sleep(10)
            
    pubsub.subscribe('web', handleWeb)

async def wifi():
    await startWifi(pubsub)
    led = Pin(1, Pin.OUT)
    while True:
        led.on()
        await asyncio.sleep_ms(500)
        led.off()
        await asyncio.sleep_ms(500)

def main():
    try:
        loop = asyncio.get_event_loop()
        
        loop.create_task(runMotor())
        loop.create_task(wifi())
        
        loop.run_forever()
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()

main()