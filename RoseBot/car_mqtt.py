from mqtt_helper import MqttClient
from rosebot import RoseBot
from datetime import datetime
import time

class App:
    def __init__(self):
        self.robot = RoseBot()
        self.is_streaming = False
        self.mode = "none"
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/copejh/#",
                                publish_topic_name="me435/copejh/to_computer",
                                use_off_campus_broker=False)

    def mqtt_callback(self, type_name, payload):
        print(f"My callback: {type_name} - {payload}")

        if type_name == "set_speeds":
            self.robot.drive_system.set_speeds(payload[0], payload[1], payload[2], payload[3])
        if type_name == "stop":
            self.robot.drive_system.stop()
        if type_name == "pan":
            self.robot.servo_head.set_pan_angle(payload)
        if type_name == "tilt":
            self.robot.servo_head.set_tilt_angle(payload)
        if type_name == "beep":
            self.robot.buzzer.beep(on_time=0.3, off_time=0.2, repeat=2)

        if type_name == "is_streaming":
            self.is_streaming = payload
            if type_name == "mode":
                self.mode = payload
                if self.mode == "none":
                    self.robot.drive_system.stop()
                elif self.mode == "drive_until_wall" or self.mode == "drive_until_line":
                    self.robot.drive_system.go(20, 20)
                    
        if type_name == "get_voltage":
            voltage = self.robot.adc.get_battery_voltage()
            self.mqtt_client.send_message("voltage", voltage)

def main():
    print("Car MQTT Lab 5")
    app = App()

    try:
        last_sensor_send_time = 0
        while True:
            time.sleep(0.01)

            if app.is_streaming:
                now = datetime.now()
                timestamp_s = now.timestamp()
                if timestamp_s - last_sensor_send_time > 2:
                    last_sensor_send_time = timestamp_s
                    date_time = now.strftime("%m-%d-%Y %H:%M:%S")
                    app.mqtt_client.send_message("line_sensor_readings", 
                                                 {"timestamp": date_time,
                                                  "left": app.robot.line_sensor.get_left(),
                                                  "middle": app.robot.line_sensor.get_middle(),
                                                  "right": app.robot.line_sensor.get_right()})

            if app.mode == "drive_until_wall":
                if app.robot.ultrasonic.get_distance() < 30:
                    app.robot.drive_system.stop()
                    app.robot.buzzer.beep(on_time=0.2, off_time=0.1, repeat=2)
                    app.mode = "none"
            elif app.mode == "drive_until_line":
                if app.robot.line_sensor.get_lineword() != "WWW":
                    app.robot.drive_system.stop()
                    app.robot.buzzer.beep(on_time=0.2, off_time=0.1, repeat=2)
                    app.mode = "none"
            elif app.mode == "line_following":
                print("Use my old code to get the sensors (ultrasonic, line sensor) and update the speeds")
                time.sleep(1.5) # For testing purposes
            elif app.mode == "light_following":
                print("Use new code to get the sensors (ultrasonic, ADC photoresistors) and update the speeds")
                time.sleep(1.5) # For testing purposes

            # # Testing the wheel set_speeds method
            # app.mqtt_client.send_message("set_speeds", [50, 50, 50, 50])
            # time.sleep(1.0)
            # app.mqtt_client.send_message("set_speeds", [-50, -50, -50, -50])
            # time.sleep(1.0)
            # app.mqtt_client.send_message("stop")
            # time.sleep(2.0)
            # # app.mqtt_client.send_message("red", "on")
            # # app.mqtt_client.send_message("yellow", 1)
            # # app.mqtt_client.send_message("green", True)
            # app.mqtt_client.send_message("leds", [1, 0, 1])
            # time.sleep(2.0)
            # # app.mqtt_client.send_message("red", "off")
            # # app.mqtt_client.send_message("yellow", 0)
            # # app.mqtt_client.send_message("green", False)
            # app.mqtt_client.send_message("leds", [0, 1, 0])
            # time.sleep(2.0)

    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()

main()