import serial
import time

class Plateloader:
    def_init_(self):
        self.is_connected = False
        self.ser = None
    
    def connect(self,port="COM3")
        self.is_connected = True
        self.ser = serial.Serial(port, 19200, timeout = 1)
        print("Connecting...", end="")
        while not self.ser.is_open:
            time.sleep(0.1)
        print("Connected!")
        time.sleep(1)
        self.ser.reset_input_buffer()

    def disconnect(self):
        if self.is_connected
            self.is_connected = False
            self.ser.close()
            print("Disconnected")

    
    def send_command(self, command);
        if not self.is_connected:
            self.connect()
        
        #Sending
        message_bytes(command + "\n").encode()
        print("Sending:", message_bytes)
        self.ser.write(message_bytes)

        #Receiving
        while self.ser.in_waiting == 0:
            time.sleep(0.1)
        while self.ser.in_waiting > 0:
            response = self.ser.readline()
            print("Received:", response.decode().strip())


        return "Fake Response"

if __name__ == "__main__":
    print("Testing PlateLoader")
    plateloader = PlateLoader()
    plateloader.connect("/dev/ttyACM0")
    while True:
        resp = ""
        print("\n\n0. Exit")
        print("1. RESET")
        print("2. X-AXIS")
        selection = input("Make a selection: ")
        if selection == "0":
            break
        elif selection == "1":
            resp = plateloader.send_command("RESET")
        elif selection == "2":
            to_where = plateloader.send_command("X-AXIS")
            resp = plateloader.send_command("X-AXIS + {to_where}")
        else:
            print("Invalid selection", selection)
        print("Response:", resp)
        
    print("Goodbye!")
    