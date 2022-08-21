from machine import Pin, PWM


class Motor:
    def __init__(self, ENA, IN1, IN2, ENB, IN3, IN4):
        # Motor A
        self.ENA = PWM(Pin(ENA))
        self.ENA.freq(1000)

        self.IN1 = Pin(IN1, Pin.OUT)
        self.IN2 = Pin(IN2, Pin.OUT)

        # Motor B
        self.ENB = PWM(Pin(ENB))
        self.ENB.freq(1000)

        self.IN3 = Pin(IN3, Pin.OUT)
        self.IN4 = Pin(IN4, Pin.OUT)

    def move(self, speedA, speedB):
        self.ENA.duty_u16(abs(65565 * speedA // 100))

        if speedA > 0:
            self.IN1.high()
            self.IN2.low()
        elif speedA < 0:
            self.IN1.low()
            self.IN2.high()
        else:
            self.IN1.low()
            self.IN2.low()

        self.ENB.duty_u16(abs(65565 * speedB // 100))

        if speedB > 0:
            self.IN3.high()
            self.IN4.low()
        elif speedB < 0:
            self.IN3.low()
            self.IN4.high()
        else:
            self.IN3.low()
            self.IN4.low()

    def stop(self):
        self.move(0, 0)
