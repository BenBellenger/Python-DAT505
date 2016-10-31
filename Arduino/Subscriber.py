from mosquitto import *
from serial import *
from random import *

ser = serial.Serial("COM3 Arduino Uno (COM3)",9600,timeout=2)
ser.write("L")

#randomID = random()
#client = Mosquitto("LightSubscriber" + str(randomID))
#client.connect("IP ADDRESS YOU ARE TOLD IN PRACTICAL")