from rosebot import RoseBot
import time

def main():
    print("Line Follower Program")
    robot = RoseBot()

    try:
        while True: 
            # Get the ultrasonic readings
            # If the distance is less than 20 cm
            #   stop the robot
            # If the distance is greater than 20 cm
            #   follow the line
            #   Get the line sensor readings
            #   Update the robot's speed based on the line sensor readings
            time.sleep(0.1)  # Sleep for a short duration to avoid busy waiting
    except KeyboardInterrupt:
        robot.drive_system.stop()  # Stop the robot on exit
        robot.drive_system.close()  # Close the drive system
        print("Program terminated.")


main()