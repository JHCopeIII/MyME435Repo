import gpiozero as gz
import time
import signal

function_using_lambda = lambda: print("Function using lambda")

def function_using_def():
    print("Function using def")
    print("As many lines of code as you want")

def led_board():
    print("Simon Says Game Starting...")
    
    # Initialize LEDs and buttons
    leds = gz.LEDBoard(14, 15, 18, pwm=False)
    button_red = gz.Button(22)
    button_yellow = gz.Button(23)
    button_green = gz.Button(24)

    # Map buttons to LEDs
    button_to_led = {
        button_red: leds[0],
        button_yellow: leds[1],
        button_green: leds[2]
    }

    sequence = []  # Store the sequence of button presses

    def button_pressed(button):
        # Add the pressed button's LED to the sequence
        led = button_to_led[button]
        sequence.append(led)
        led.on()  # Light up the LED
        time.sleep(0.5)
        led.off()  # Turn off the LED

    # Assign button press handlers
    button_red.when_pressed = lambda: button_pressed(button_red)
    button_yellow.when_pressed = lambda: button_pressed(button_yellow)
    button_green.when_pressed = lambda: button_pressed(button_green)

    print("Press buttons to create a sequence. Press Ctrl+C to stop and let the computer play.")

    try:
        # Wait for the user to input the sequence
        signal.pause()
    except KeyboardInterrupt:
        print("\nPlaying back the sequence...")

        # Replay the sequence using LEDs
        for led in sequence:
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(0.2)

    print("Game Over!")

def button_events():
     print("Button Events")
     button = gz.Button(25)
     # button.when_pressed = lambda: print("Button pressed")
     # button.when_released = lambda: print("Button released")
     # button.when_held = lambda: some_helper_function(led_board, 0.5)

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
