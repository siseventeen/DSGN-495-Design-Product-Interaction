import board
import busio
import adafruit_apds9960.apds9960
import neopixel
import time
import random
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.5
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_color = True

pixel_pin = board.A1 # neopixel can be driven by any pin
num_pixels = 8
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)
    
while True:
    current_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for i in range(0,7):
        pixels.fill(current_color)
        pixels.show()  
        r, g, b, c = sensor.color_data
        led_color= (int(r/65535*255),int(g/65535*255),int(b/65535*255))
        led[0]=led_color
        time.sleep(2)
        print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c)) 
        print('neopixel_color:'+str(current_color)+' led_color:'+str(led_color))
           

