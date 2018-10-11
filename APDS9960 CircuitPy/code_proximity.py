import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True

brightness = 0.02

pixel_pin = board.A1 # neopixel can be driven by any pin
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0, auto_write=False)
current_color = (180, 0, 255)

while True:
    pixels.brightness=round(sensor.proximity()/255 * 0.9 + pixels.brightness*0.1,2)
    pixels.fill(current_color)
    pixels.show()
    #print(current_color)
    print('brightness:'+str(pixels.brightness)+'  proximity:'+str(sensor.proximity()))

    time.sleep(0.1)