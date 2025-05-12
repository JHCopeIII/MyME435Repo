from spi_ledpixel import Freenove_SPI_LedPixel
import gpiozero as gz
import time

class CarLeds:

    def __init__(self):
        #pin18 = gz.InputDevice(18, pull_up=False)
        #time.sleep(3)
        self.neopixel_strip = Freenove_SPI_LedPixel(bright=128)
        
    def set_all_leds(self, red, green, blue):
        self.neopixel_strip.set_all_led_color(red, green, blue)

    def set_leds(self, led_index, red, green, blue):
        self.neopixel_strip.set_led_color(red, green, blue)  

    def turn_off(self):
        self.set_all_leds(0, 0, 0)

if __name__ == "__main__":
    car_leds = CarLeds()
    car_leds.set_all_leds(255, 0, 0)  # Set all LEDs to red
    time.sleep(1)
    car_leds.set_leds, (0, 255, 0)  # Set all LEDs to green
    time.sleep(1)
    car_leds.set_leds(0, 0, 0, 255)  # Set all LEDs to blue
    time.sleep(1)
    car_leds.turn_off  # Turn off all LEDs