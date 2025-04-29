from mqtt_helper import MqttClient
import gpiozero as gz
import time

class App:
    def __init__(self):
        self.red_led = gz.LED(14)
        self.yellow_led = gz.LED(15)
        self.green_led = gz.LED(18)

        self.button_23 = gz.Button(23)
        self.button_23.when_pressed = self.button_23_pressed
        self.button_25 = gz.Button(25)
        self.button_25.when_pressed = lambda: self.mqtt_client.send_message("reset")

        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/copejh/#",
                                publish_topic_name="me435/copejh/to_computer",
                                use_off_campus_broker=False)

        def button_23_pressed(self):
            print("Button 23 pressed")
            self.mqtt_client.send_message("button_23")
        

        def mqtt_callback(self, type_name, payload):
            print(f"My callback: {type_name} - {payload}")

            if type_name == "red":
                if payload == "on":
                    self.red_led.on()
                elif payload == "off":
                    self.red_led.off()
                else:
                    print("Unknown payload for red LED:", payload)
            
            if type_name == "yellow":
                if payload == "on":
                    self.yellow_led.on()
                elif payload == "off":
                    self.yellow_led.off()
                else:
                    print("Unknown payload for yellow LED:", payload)

            if type_name == "green":
                if payload == "on":
                    self.green_led.on()
                elif payload == "off":
                    self.green_led.off()
                else:
                    print("Unknown payload for green LED:", payload)

            if type_name == "leds":
                if payload[0] == 0:
                    self.red_led.off()
                elif payload[0] == 1:
                    self.red_led.on()

                if payload[1] == 0:
                    self.yellow_led.off()
                elif payload[1] == 1:
                    self.yellow_led.on()

                if payload[2] == 0:
                    self.green_led.off()
                elif payload[2] == 1:
                    self.green_led.on()
        

def main():
    print("GPIO MQTT Test")
    app = APP()

    try:
        while True:
            time.sleep(0.1)
            #app.mqtt_client.send_message("red", "on")
            #app.mqtt_client.send_message("yellow", 1)
            #app.mqtt_client.send_message("green", True)
            app.mqtt_client.send_message("leds", [1, 0, 1])
            time.sleep(2.0)
            #app.mqtt_client.send_message("red", "off")
            #app.mqtt_client.send_message("yellow", 0)
            #app.mqtt_client.send_message("green", False)
            app.mqtt_client.send_message("leds", [0, 1, 0])
            time.sleep(2.0)


    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()

main()