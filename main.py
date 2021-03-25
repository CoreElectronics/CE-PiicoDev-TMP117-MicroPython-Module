# PiicoDev TMP117 minimal example code
# This program reads the temperature from the PiicoDev TMP117 precision temperature sensor
# and displays the result in Degrees Celsius, Farenheit and Kelvin

# from microbit import *
from tmp117 import *
from utime import sleep_ms

mySensor = tmp117()

while True:
    # Read and print the temperature in various units
    tempC = mySensor.readTempC() # Celsius
    tempF = mySensor.readTempF() # Farenheit
    tempK = mySensor.readTempK() # Kelvin
    
    tempStringC = str(tempC) # convert temperature number to string
    tempStringF = str(tempF)
    tempStringK = str(tempK)
    
    print("It's " + tempStringC + "°C")
    
    sleep_ms(1000)