# PiicoDev TMP117 minimal example code
# This program reads the temperature from the PiicoDev TMP117 precision temperature sensor
# and displays the result in Degrees Celsius, Farenheit and Kelvin

from PiicoDev_TMP117 import PiicoDev_TMP117
from utime import sleep_ms

temp = PiicoDev_TMP117()


while True:
    # Read and print the temperature in various units
    tempC = temp.readTempC() # Celsius
    tempF = temp.readTempF() # Farenheit
    tempK = temp.readTempK() # Kelvin
    
    tempStringC = str(tempC) # convert temperature number to string
    tempStringF = str(tempF)
    tempStringK = str(tempK)
    
    print("It's " + tempStringC + "°C")
    
    sleep_ms(1000)