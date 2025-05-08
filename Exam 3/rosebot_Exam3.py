from rosebot_drive_system_Exam3 import DriveSystem
from rosebot_sensors_Exam3 import Ultrasonic

class RoseBot:
    def __init__(self):
        print("Creating a RoseBot")
        self.drive_system = DriveSystem()
        self.ultrasonic = Ultrasonic()