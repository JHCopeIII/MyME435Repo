import gpiozero as gz
import time
import signal

function_using_lambda = lambda: print("Function using lambda")

def function_using_def():
    print("Function using def")
    print("As many lines of code as you want")

def led_board():
    print("LED Board")
    led_board = gz.LEDBoard(14, 15, 18, pwm=True)
    button_red = gz.Button(22)
    button_yellow = gz.Button(23)
    button_green = gz.Button(24)
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

def button_events():
     print("Button Events")
     button = gz.Button(25)
     # button.when_pressed = lambda: print("Button pressed")
     # button.when_released = lambda: print("Button released")
     # button.when_held = lambda: print("Button held")

     button.when_pressed = function_using_def
     button.when_released = function_using_lambda
     button.when_held = lambda: some_helper_function(led_board, 0.5)
     signal.pause()

def button_states():
    print("Button States")
    button = gz.Button(25)
    
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
        time.sleep(0.5)

def main():
        print("Pushbuttons")
        # button_states()
        button_events()


main()
