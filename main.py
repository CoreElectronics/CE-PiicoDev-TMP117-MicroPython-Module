# PiicoDev TMP117 minimal example code
# This program reads the temperature from the PiicoDev TMP117 precision temperature sensor
# and displays the result in Degrees Celsius, Farenheit and Kelvin

from PiicoDev_TMP117 import PiicoDev_TMP117
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

tempSensor = PiicoDev_TMP117() # initialise the sensor

while True:
    # Read and print the temperature in various units
    tempC = tempSensor.readTempC() # Celsius
    tempF = tempSensor.readTempF() # Farenheit
    tempK = tempSensor.readTempK() # Kelvin
    
    # Convert temperature into a string and print the data
    print(str(tempC) + " °C")
    
    sleep_ms(1000) # delay 1 second
