from machine import Pin
import time
import random

led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(11, Pin.OUT)
led4 = Pin(10, Pin.OUT)
led5 = Pin(9, Pin.OUT)

segments = [led1, led2, led3, led4, led5]

while True:
    rand_num = random.randint(0,4)
    segments[rand_num].value(1)
    time.sleep(0.08)
    segments[rand_num].value(0)
