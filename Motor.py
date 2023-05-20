import RPi.GPIO as GPIO
from time import sleep


class Motor:
    inA = 0
    inB = 0
    channel_setup = False

    def __init__(self, a, b):
        self.inA = a
        self.inB = b
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.inA, GPIO.OUT)
        GPIO.setup(self.inB, GPIO.OUT)
        GPIO.output(self.inA, GPIO.LOW)
        GPIO.output(self.inB, GPIO.LOW)
        print("Setup Complete")

    def move_forward(self, time=0):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.inA, GPIO.HIGH)
        GPIO.output(self.inB, GPIO.LOW)
        self.channel_setup = True
        sleep(time)

    def move_backward(self, time=0):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.inA, GPIO.LOW)
        GPIO.output(self.inB, GPIO.HIGH)
        self.channel_setup = True
        sleep(time)

    def stop(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.inA, GPIO.LOW)
        GPIO.output(self.inB, GPIO.LOW)
        self.channel_setup = False

    def __del__(self):
        if (self.channel_setup):
            GPIO.cleanup()
