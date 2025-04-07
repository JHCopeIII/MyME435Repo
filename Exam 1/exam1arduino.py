import serial
import time

class ArduinoCommander:
    def __init__(self):
        self.is_connected = False
        self.ser = None
        
    def connect(self, port="ttyACM0"):
        print("Connecting... ", end="")
        self.ser = serial.Serial(port, baudrate=19200, timeout=2)
        while not self.ser.is_open:
            time.sleep(0.1)
        self.is_connected = True
        print("Connected!")
        time.sleep(1)
        self.ser.reset_input_buffer()
    
    def disconnect(self):
        if self.is_connected:
            self.ser.close()
            self.is_connected = False
            print("Disconnected")
        
    def send_command(self, command):
        if not self.is_connected:
            self.connect()
            
        message_bytes = (command.strip() + "\n").encode()
        print("Sending:", message_bytes)
        self.ser.write(message_bytes)
        
        # Await response
        lines = []
        start_time = time.time()
        while time.time() - start_time < 5:  # Timeout of 5 seconds
            while self.ser.in_waiting > 0:
                response = self.ser.readline().decode().strip()
                if response:
                    print("Received:", response)
                    lines.append(response)
            if lines:
                break
            time.sleep(0.1)
        return lines

if __name__ == "__main__":
    print("Arduino Command Console\n")
    arduino = ArduinoCommander()
    arduino.connect("ttyACM0")

    while True:
        print("\nOptions:")
        print("0. Exit")
        print("1. Turn LED ON")
        print("2. Turn LED OFF")
        print("3. FLASH LED")
        print("4. MOVE Command (Simulated)")
        selection = input("Make a selection: ").strip()

        if selection == "0":
            break
        elif selection == "1":
            arduino.send_command("LED ON")
        elif selection == "2":
            arduino.send_command("LED OFF")
        elif selection == "3":
            try:
                count = int(input("Number of flashes: "))
                period = int(input("Delay per flash (ms): "))
                arduino.send_command(f"FLASH {count} {period}")
            except ValueError:
                print("Please enter valid integers.")
        elif selection == "4":
            location = input("Enter simulated move position: ").strip()
            arduino.send_command(f"MOVE {location}")
        else:
            print("Invalid selection.")

    arduino.disconnect()
    print("Goodbye!")
