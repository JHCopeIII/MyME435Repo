from motor import OrdinaryCar
import time

class DriveSystem:

    def __init__(self):
        print("Creating a DriveSystem")
        self.car = OrdinaryCar()

    def scale_speed(self, speed):
        return int(speed / 100 * 4095)

    def set_speeds(self, lf, lr, rf, rr):
        lf_duty = self.scale_speed(lf)
        lr_duty = self.scale_speed(lr)
        rf_duty = self.scale_speed(rf)
        rr_duty = self.scale_speed(rr)
    
    def go(self, left_speed, right_speed):
        left_duty = self.scale_speed(left_speed)
        right_duty = self.scale_speed(right_speed)
        self.car.set_motor_model(left_duty, left_duty, right_duty, right_duty)

    def stop(self):
        self.set_speeds(0,0,0,0)

    def go_straight_for_seconds(self, seconds, speed):
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()

    def strafe_left(self, speed):
        duty = self.scale_speed(speed)
        self.car.set_motor_model(-duty, duty, duty, -duty)
    
    def strafe_right(self, speed):
        duty = self.scale_speed(speed)
        self.car.set_motor_model(duty, -duty, -duty, duty)

    def go_straight_for_inches(self, inches, speed):
        m = 0.5  # meters per second
        B = 0.5
        inches_per_second = m * speed + B
        seconds = inches / inches_per_second
        self.go_straight_for_seconds(seconds, speed)

    def spin_in_place_for_seconds(self, seconds, speed, isLeft = True):
        duty = self.scale_speed(speed)
        if isLeft:
            self.car.set_motor_model(-duty, -duty, duty, duty)
        else:
            self.car.set_motor_model(duty, duty, -duty, -duty)
        time.sleep(seconds)
        self.stop()

    def spin_in_place_for_degrees(self, degrees, isLeft = True):
        m = 0.5
        B = 0.5
        degrees_per_second = m * degrees + B
        seconds = degrees / degrees_per_second
        self.spin_in_place_for_seconds(seconds, speed, isLeft)

    def stop(self):
        self.car.set_motor_model(0, 0, 0, 0)

    def close(self):
        self.car.close()
