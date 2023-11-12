

import serial
import time

microcontroller = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)


def write_read(x):
    microcontroller.write(bytes(x, "utf-8"))
    time.sleep(0.01)


while True:
    msg = input("cxxx,yyy")
    write_read(msg)
    print(str(microcontroller.readline()))