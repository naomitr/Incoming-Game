import serial
while True:
    val = input("Enter 0 or 1 to control LED: ")
    print(int(val))
    serial.Serial('COM6',9600)
