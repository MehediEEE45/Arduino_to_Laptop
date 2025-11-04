# pip install pyserial
import serial
import serial.tools.list_ports
import threading

# List all available ports
ports = serial.tools.list_ports.comports()
portsList = [str(port) for port in ports]

print("Available COM ports:")
for port in portsList:
    print(port)

# Select COM port
com = input("Select COM port for Arduino #: ").strip()
use = None
for port in portsList:
    if port.startswith("COM" + com):
        use = "COM" + com
        print("Using port:", use)
        break

if use is None:
    print("Invalid COM port!")
    exit()

# Open serial connection
serialInst = serial.Serial(port=use, baudrate=9600, timeout=1)
print("Connected to Arduino on", use)

# Function to continuously read data from Arduino
def read_from_arduino():
    while True:
        try:
            if serialInst.in_waiting > 0:
                data = serialInst.readline().decode('utf-8').strip()
                if data:
                    print("\nArduino says:", data)
        except Exception as e:
            print("Error reading:", e)
            break

# Start thread to read Arduino data
thread = threading.Thread(target=read_from_arduino, daemon=True)
thread.start()

# Main loop to send commands to Arduino
try:
    while True:
        command = input("Arduino Command (ON/OFF/exit): ").strip()
        if not command:
            continue

        # Send command
        serialInst.write((command + '\n').encode('utf-8'))

        if command.lower() == 'exit':
            print("Exiting...")
            break
finally:
    serialInst.close()
    print("Serial port closed.")
