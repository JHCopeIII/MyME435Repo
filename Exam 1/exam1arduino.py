import serial
import time

class ArduinoCommander:
    def __init__(self):
        self.is_connected = False
        self.ser = None
        
    def connect(self, port="/dev/ttyACM0"):
        self.is_connected = True
        self.ser = serial.Serial(port, baudrate=19200)
        print("Connecting... ", end="")
        while not self.ser.is_open:
            time.sleep(0.1)
        print("Connected!")
        time.sleep(3)
        self.ser.reset_input_buffer()
    
    def disconnect(self):
        if self.is_connected:
            self.ser.close()
            self.is_connected = False
            print("Disconnected")
        
    def send_command(self, command):
        if not self.is_connected:
            self.connect()
            
        # Sending
        message_bytes = (command + "\n").encode()
        print("Sending:", message_bytes)
        self.ser.write(message_bytes)
        
        # Receiving
        while self.ser.in_waiting == 0:
            time.sleep(0.1)
        while self.ser.in_waiting > 0:
            response = self.ser.readline()
            print("Received:", response.decode().strip())
        return response

if __name__ == "__main__":
    print("Arduino Command Console")
    exam1arduino = ArduinoCommander()
    exam1arduino.connect("/dev/ttyACM0")
    while True:
        resp = ""
        print("\n\n0. Exit")
        print("1. Turn LED ON")
        print("2. Turn LED OFF")
        print("3. FLASH LED")
        selection = input("Make a selection: ")
        if selection == "0":
            break
        elif selection == "1":
            resp = exam1arduino.send_command("LED ON")
        elif selection == "2":
            resp = exam1arduino.send_command("LED OFF")
        elif selection == "3":
            try:
                count = int(input("Number of flashes: "))
                period = int(input("Delay per flash (ms): "))
                resp = exam1arduino.send_command(f"FLASH {count} {period}")
            except ValueError:
                print("Please enter valid integers.")
        else:
            print("Invalid selection.")

    print("Goodbye!")
