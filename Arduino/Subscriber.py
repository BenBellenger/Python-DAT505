from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("FULL DEVICE NAME",SPEED,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("IP ADDRESS YOU ARE TOLD IN PRACTICAL")

# The rest of your code goes in here !!!