import serial 

ser = serial.Serial("COM3 Arduino Uno (COM3)",9600,timeout=2)
ser.write("L")