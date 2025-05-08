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
            # Turn the left wheels forward
            time, pwm = payload
            self.robot.drive_system.left_motor.forward(pwm, time)

        elif type_name == "left_backward":
            # Turn the left wheels backward
            time, pwm = payload
            self.robot.drive_system.left_motor.backward(pwm, time)

        elif type_name == "right_forward":
            # Turn the right wheels forward
            time, pwm = payload
            self.robot.drive_system.right_motor.forward(pwm, time)

        elif type_name == "right_backward":
            # Turn the right wheels backward
            time, pwm = payload
            self.robot.drive_system.right_motor.backward(pwm, time)

        elif type_name == "all_forward":
            # Turn all four wheels forward
            time, left_pwm, right_pwm = payload
            self.robot.drive_system.set_speeds(left_pwm, right_pwm, time)

        elif type_name == "all_backward":
            # Turn all four wheels backward
            time, left_pwm, right_pwm = payload
            self.robot.drive_system.set_speeds(-left_pwm, -right_pwm, time)

            

def main():
    print("Exam 3 - Waiting for commands from MATLAB App Designer")
    app = App()

    try:
        # Keep the program running to receive MQTT messages
        while True:
            time.sleep(0.1)  # Prevent high CPU usage

    except KeyboardInterrupt:
        print("Exiting...")
        app.mqtt_client.close()

main()