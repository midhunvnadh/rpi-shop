import RPi.GPIO as GPIO
import time

pin = 36

while(True):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, True)
    time.sleep(2)
    GPIO.output(pin, False)