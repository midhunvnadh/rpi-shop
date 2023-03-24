#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json

reader = SimpleMFRC522()

def write_nfc():
    try:
            item_name = input('Item Name:')
            item_price = input('Item Price:')
            json_val = json.dumps({'item':item_name, 'price': item_price})
            print("Now place your tag to write")
            reader.write(json_val)
            print("Written")
    finally:
            GPIO.cleanup()