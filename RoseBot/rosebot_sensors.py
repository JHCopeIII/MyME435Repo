from gpiozero import gz
import time

class Ultrasonic:
    def __init__(self):
        self.distance_sensor = gz.DistanceSensor(echo=22, trigger=17)

    def get_distance(self):
        return self.distance_sensor.distance * 100

class Linesensor:
    
    def _init__(self):
        self.was_line_left = True
        self.left = gz.LineSensor(14)
        self.middle = gz.LineSensor(15)
        self.right = gz.LineSensor(23)

    def get_left(self):
        if self.left.value == 1:
            return "B"
        return "W"
    
    def get_middle(self):
        if self.middle.value == 1:
            return "B"
        return "W"
    
    def get_right(self):
        if self.right.value == 1:
            return "B"
        return "W"
    
    def get_lineword(self):
        return self.get_left() + self.get_middle() + self.get_right()
    
    def get_values(self):
        lineword = self.get_lineword
        if lineword == "WWW":
            if self.was_line_left:
                return -3
            return 3
        elif lineword == "BWW":
            self.was_line_left = True
            return -2
        elif lineword == "BBW":
            self.was_line_left = True
            return -1
        elif lineword == "WBW":
            return 0
        elif lineword == "WBB":
            self.was_line_left = False
            return 1
        elif lineword == "WWB":
            self.was_line_left = False
            return 2
        else:
            return 0
    

if __name__ == "__main__":
    ultrasonic = Ultrasonic()
    while True:
        distance = ultrasonic.get_distance()
        print(f"Distance = {ultrasonic.get_distance()} cm")
        print(f"Line word = {Linesensor.get_lineword()} value = {Linesensor.get_values()}")
        time.sleep(0.1)  # Sleep for a short duration to avoid busy waiting