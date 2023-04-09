#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
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
    except:
        print("Error Occoured!")
        GPIO.cleanup()
        return read_nfc()
    finally:
        GPIO.cleanup()
    return item, price

