from mqtt_helper import MqttClient
from rosebot_Exam3 import RoseBot
import time

class App:
    def __init__(self):
        self.robot = RoseBot()
        self.mqtt_client = MqttClient()
        self.mqtt_client.callback = self.mqtt_callback
        self.mqtt_client.connect(subscription_topic_name="me435/copejh/#",
                                publish_topic_name="me435/copejh/to_computer",
                                use_off_campus_broker=False)
        

    def mqtt_callback(self, type_name, payload):
        print(f"My callback: {type_name} - {payload}")

        if type_name == "left_forward":
            # Move the left wheels forward
            duration, pwm = payload
            self.robot.drive_system.go(pwm, 0)  # Positional arguments: left_speed, right_speed
            time.sleep(duration)
            self.robot.drive_system.stop()

        elif type_name == "left_backward":
            # Move the left wheels backward
            duration, pwm = payload
            self.robot.drive_system.go(-pwm, 0)  # Negative speed for backward
            time.sleep(duration)
            self.robot.drive_system.stop()

        elif type_name == "right_forward":
            # Move the right wheels forward
            duration, pwm = payload
            self.robot.drive_system.go(0, pwm)  # Left speed is 0, right speed is pwm
            time.sleep(duration)
            self.robot.drive_system.stop()

        elif type_name == "right_backward":
            # Move the right wheels backward
            duration, pwm = payload
            self.robot.drive_system.go(0, -pwm)  # Negative speed for backward
            time.sleep(duration)
            self.robot.drive_system.stop()

        elif type_name == "both_forward":
            # Move both wheels forward
            duration, left_pwm, right_pwm = payload
            self.robot.drive_system.go(left_pwm, right_pwm)  # Both speeds are positive
            time.sleep(duration)
            self.robot.drive_system.stop()

        elif type_name == "both_backward":
            # Move both wheels backward
            duration, left_pwm, right_pwm = payload
            self.robot.drive_system.go(-left_pwm, -right_pwm)  # Negative speeds for backward
            time.sleep(duration)
            self.robot.drive_system.stop()
         
    def send_ultrasonic_reading(self):
        try:
            distance = self.robot.ultrasonic.distance_sensor.distance * 100  # Correct: Accessing the distance attribute
            if distance is not None:
                print(f"Ultrasonic distance: {distance} cm")
                self.mqtt_client.send_message("ultra", distance)
            else:
                print("Ultrasonic sensor returned None (no echo).")
        except Exception as e:
            print(f"Error reading ultrasonic sensor: {e}")


def main():
    print("Exam 3 - Waiting for commands from MATLAB App Designer")
    app = App()

    try:
        # Keep the program running to receive MQTT messages
        while True:
            time.sleep(0.1)  # Prevent high CPU usage
            app.send_ultrasonic_reading()
            time.sleep(2.0)
            app.mqtt_client.send_message("left_forward", [1, 40])
            time.sleep(2.0)
            app.mqtt_client.send_message("left_backward", [1, 40])
            time.sleep(2.0)
            app.mqtt_client.send_message("right_forward", [1, 40])
            time.sleep(2.0)
            app.mqtt_client.send_message("right_backward", [1, 40])
            time.sleep(2.0)
            app.mqtt_client.send_message("both_forward", [1, 40, 40])
            time.sleep(2.0)
            app.mqtt_client.send_message("both_backward", [1, 40, 40])
            time.sleep(2.0)

    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()

main()