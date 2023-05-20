from read import read_nfc
from time import sleep

import requests


def addToCart(name, price):
    r = requests.put(
        f"https://rpi-shopcart-web.vercel.app/api/products?name={name}&quantity=1&price={price}")
    print(r.json())


def rfid():
    while (True):
        try:
            name, price = read_nfc()
            addToCart(name, price)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
        sleep(1)
