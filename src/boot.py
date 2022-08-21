from machine import Pin, PWM
import uasyncio as asyncio

from motor import Motor
from wifi import startWifi
from pubsub import PubSub

pubsub = PubSub()
motor = Motor(ENA=2, IN1=3, IN2=4, ENB=7, IN3=5, IN4=6)


async def mainLoop():
    while True:
        data = await pubsub.wait('web')
        if data == 'forward':
            motor.move(50, 50)
        elif data == 'backward':
            motor.move(-50, -50)
        elif data == 'left':
            motor.move(0, 50)
        elif data == 'right':
            motor.move(50, 0)
        elif data == 'stop':
            motor.move(0, 0)


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
        loop.create_task(mainLoop())
        loop.create_task(wifi())
        loop.run_forever()
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()


main()
