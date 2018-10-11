import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import time
import math

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True
sensor.enable_gesture = True

brightness = 0.02

pixel_pin = board.A1 # neopixel can be driven by any pin
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)
current_color = (10, 10, 10)

def change_color_up(color):
    if color[0]+40 <=255:
        color=(color[0]+40,color[1],color[2])
    return color

def change_color_down(color):
    if color[0]-40 >=0:
        color=(color[0]-40,color[1],color[2])
    return color

def change_color_right(color):
    if color[2]+40 <=255:
        color=(color[0],color[1],color[2]+40)
    return color
    
def change_color_left(color):
    if color[2]-40 >=0:
        color=(color[0],color[1],color[2]-40)
    return color
    
while True:
    gesture = sensor.gesture()
    if gesture == 1: 
        current_color=change_color_up(current_color)    
        print("up")
        print(current_color)
    elif gesture == 2:
        current_color=change_color_down(current_color) 
        print("down")
        print(current_color)
    elif gesture == 3:
        current_color=change_color_left(current_color) 
        print("left")
        print(current_color)
    elif gesture == 4:
        current_color=change_color_right(current_color) 
        print("right")
        print(current_color)
    pixels.fill(current_color)
    pixels.show()
    time.sleep(0.05)
    