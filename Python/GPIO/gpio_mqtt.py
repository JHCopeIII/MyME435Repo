from mqtt_helper import MqttClient
import time

class APP:
    def __init__(self):
        self.red_led = gz.LED(14)

        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/copejh/#",
                                publish_topic_name="me435/copejh/to_computer",
                                use_off_campus_broker=False)

        def mqtt_callback(self, type_name, payload):
            print(f"My callback: {type_name} - {payload}")
            if type_name == "red":
                if payload == "on":
                    self.red_led.on()
                elif payload == "off":
                    self.red_led.off()
                else:
                    print("Unknown payload for red LED:", payload)
            else:
                print("Unknown type: {payload}")
        

def main():
    print("GPIO MQTT Test")
    app = APP()

    try:
        while True:
            time.sleep(0.1)
            #app.mqtt_client.send_message("red", "on")
            #time.sleep(2.0)
            #app.mqtt_client.send_message("red", "off")
            #time.sleep(2.0)


    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()

main()