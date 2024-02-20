import time
import random # not the same as CPython random :) - no shuffle
from adafruit_circuitplayground.express import cpx

def randRGB(min=0, max=255):
    return random.randint(0, 255)

def randLED(min=0, max=255):
    return tuple((randRGB(min, max) for x in range(3)))
    
def light(is_reverse=False, is_random=False):
    order = range(len(cpx.pixels))
    if is_reverse:
        order = reversed(order)
    if is_random:
        order = list(order)
        new_order = []
        while len(order):
            new_order.append(order.pop(random.randint(0, len(order) - 1)))
        order = new_order
    for idx in order:
        cpx.pixels[idx] = randLED()
        time.sleep(0.1)
    
def wipe(is_reverse=False, is_random=False):
    order = range(len(cpx.pixels))
    if is_reverse:
        order = reversed(order)
    if is_random:
        order = list(order)
        new_order = []
        while len(order):
            new_order.append(order.pop(random.randint(0, len(order) - 1)))
        order = new_order
    for idx in order:
        cpx.pixels[idx] = (0,0,0)
        time.sleep(0.1)
    
while True:
    # cpx.red_led = not cpx.red_led
    time.sleep(0.1)
    test = randLED()
    for _ in range(2):
        light()
        wipe(is_reverse=True)
    for _ in range(2):
        light()
        wipe()
    for _ in range(2):
        light(is_random=True)
        wipe(is_random=True)

        
    