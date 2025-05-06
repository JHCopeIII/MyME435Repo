from servo import Servo
import time

class ServoHead:
    def __init__(self):
        self.servo = Servo()

    def set_pan_angle(self, degrees):
        self.servo.set_servo_pwm('0', degrees)

    def set_tilt_angle(self, degrees):
        self.servo.set_servo_pwm('1', degrees)

    def reset(self):
        self.set_pan_angle(90)
        self.set_tilt_angle(90)
        
if __name__ == "__main__":
    print("Servo head initialized. Press Ctrl-C to exit.")
    servo_head = ServoHead()
    try:
        while True:
            # Example usage
            servo_head.reset()
            time.sleep(1)
            servo_head.set_pan_angle(30)
            servo_head.set_tilt_angle(30)
            time.sleep(2)
            servo_head.set_pan_angle(150)
            servo_head.set_tilt_angle(150)
            time.sleep(2)
            servo_head.reset()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting program.")