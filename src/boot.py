# boot.py -- run on boot-up

from machine import Pin, PWM
from time import sleep

from motor import Motor

print("Robot car")

motor = Motor(2, 3, 4, 7, 5, 6)

motor.move(50, 50)

sleep(2)

motor.move(100, 100)

sleep(2)

motor.move(-100, 100)

sleep(2)

motor.move(100, -100)

sleep(2)

motor.stop()

