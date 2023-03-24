#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json

reader = SimpleMFRC522()

def read_nfc():
    try:
        print("Place the tag!")        
        id, text = reader.read()
        value = json.loads(text)
        item = value["item"]
        price = value["price"]
        print(item, price)
    finally:
        GPIO.cleanup()