from max31865 import max31865
import RPi.GPIO as GPIO
import time
csPin = 8
misoPin = 9
mosiPin = 10
clkPin = 11
max = max31865.max31865(csPin,misoPin,mosiPin,clkPin)
for i in range(10):
    tempC = max.readTemp()
    print("temp C:")
    print(tempC)
    time.sleep(0.1)
GPIO.cleanup()
