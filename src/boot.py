# boot.py -- run on boot-up

from machine import Pin, PWM
from time import sleep

INR1 = Pin(3, Pin.OUT)
INR2 = Pin(4, Pin.OUT)

ENR = PWM(Pin(2))
ENR.freq(1000)

INL1 = Pin(5, Pin.OUT)
INL2 = Pin(6, Pin.OUT)

ENL = PWM(Pin(7))
ENL.freq(1000)

ENR.duty_u16(32768)
INR1.high()
INR2.low()

ENL.duty_u16(32768)
INL1.high()
INL2.low()

sleep(3)

ENR.duty_u16(32768)
INR1.low()
INR2.low()

ENL.duty_u16(32768)
INL1.high()
INL2.low()

sleep(1)

ENR.duty_u16(32768)
INR1.high()
INR2.low()

ENL.duty_u16(32768)
INL1.high()
INL2.low()

sleep(3)

ENR.duty_u16(32768)
INR1.high()
INR2.low()

ENL.duty_u16(32768)
INL1.low()
INL2.low()

sleep(1)

ENR.duty_u16(32768)
INR1.high()
INR2.low()

ENL.duty_u16(32768)
INL1.high()
INL2.low()

sleep(3)

ENR.duty_u16(32768)
INR1.low()
INR2.low()

ENL.duty_u16(65535)
INL1.low()
INL2.low()

