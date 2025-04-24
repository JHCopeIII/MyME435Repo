from rosebot_drive_system import DriveSystem
from rosebot_sensors import Ultrasonic, Linesensor

class RoseBot:

    def __init__(self):
        print("Creating a RoseBot")
        self.drive_system = DriveSystem()
        self.ultrasonic = Ultrasonic()
        self.line_sensor = Linesensor()