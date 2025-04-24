import gpiozero as gz
import time
import signal

leds = {
    "red": gz.LED(14),
    "yellow": gz.LED(15),
    "green": gz.LED(18)
}

buttons = {
    "red": gz.Button(22),
    "yellow": gz.Button(23),
    "green": gz.Button(24)
}

colors = ["red", "yellow", "green"]
sequence = []
user_input_enabled = True

def flash_led(color, duration=0.5):
    leds[color].on()
    time.sleep(duration)
    leds[color].off()
    time.sleep(0.2)

def play_sequence():
    global user_input_enabled
    user_input_enabled = False
    for color in sequence:
        flash_led(color)
    user_input_enabled = True

def on_button_press(color):
    def handler():
        global user_input_enabled
        if user_input_enabled:
            leds[color].on()
            time.sleep(0.3)
            leds[color].off()
            sequence.append(color)
            time.sleep(0.3)
            play_sequence()
    return handler

def simon_says_event_version():
    print("Simon Says Start")

    for color in colors:
        buttons[color].when_pressed = on_button_press(color)

    try:
        signal.pause() 
    except KeyboardInterrupt:
        print("\nGame Over")

if __name__ == "__main__":
    simon_says_event_version()
