# boot.py -- run on boot-up

from machine import Pin, PWM
from time import sleep
import uasyncio as asyncio

from motor import Motor

async def runMotor():
    motor = Motor(2, 3, 4, 7, 5, 6)

    motor.move(50, 50)

    await asyncio.sleep(2)

    motor.move(100, 100)

    await asyncio.sleep(2)

    motor.move(-100, 100)

    await asyncio.sleep(2)

    motor.move(100, -100)

    await asyncio.sleep(2)
    
    motor.stop()

async def main():
    asyncio.create_task(runMotor())
    await asyncio.sleep(10)

asyncio.run(main())
