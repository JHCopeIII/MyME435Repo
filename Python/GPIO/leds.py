import gpiozero as gz
import time
import signal

def led_board():
    print("LED Board")
    led_board = gz.LEDBoard(14, 15, 18, pwm=True)
    for k in range(5):
        led_board.on()
        time.sleep(1)
        led_board.off()
        time.sleep(1)
        led_board.value = (1, 0, 1)
        time.sleep(1)
        led_board.value = (0, 0, 0.5)
        time.sleep(1)

    signal.pause()

def fancy_leds():
    print("Fancy LEDs")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)

    red_led.blink(on_time=1.0, off_time=0.5)
    time.sleep(0.15)
    yellow_led.blink(on_time=1.0, off_time=0.5)
    time.sleep(0.3)
    green_led.blink(on_time=1.0, off_time=0.5)
    signal.pause()



def basic_on_off():
    print("Basic on/off")
    red_led = gz.DigitalOutputDevice(14)
    yellow_led = gz.DigitalOutputDevice(15)
    green_led = gz.DigitalOutputDevice(18)

    red_led.on()
    yellow_led.on()
    green_led.on()
    time.sleep(3)
    red_led.off()
    yellow_led.off()
    green_led.off()
    time.sleep(1)
    


def main():
    print("LEDS")
    # basic_on_off()
    # fancy_leds()
    led_board()
    print("End of LEDS")


main()