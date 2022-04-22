# PiicoDev TMP117 - reading multiple sensors
# This program independently reads the temperature from two PiicoDev TMP117 precision temperature sensors
# Each sensor should have its ASW switches configured to match the asw argument during initialisaiton, eg.
# sensorA: asw=[1,0,0,0] so the first switch should be ON and the rest OFF
# sensorB: asw=[0,1,0,0] so the second switch should be ON and the rest OFF
# this logic expands to a maximum of four sensors

from PiicoDev_TMP117 import PiicoDev_TMP117
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

sensorA = PiicoDev_TMP117(asw=[1,0,0,0]) # initialise the sensor
sensorB = PiicoDev_TMP117(asw=[0,1,0,0]) # initialise the sensor

# Advanced users may prefer to set the address explicitly, instead:
# sensorA = PiicoDev_TMP117(address=0x48) # initialise the sensor
# sensorB = PiicoDev_TMP117(address=0x49) # initialise the sensor

while True:
    # Read and print the temperature in various units
    tempA = sensorA.readTempC() # read from sensor A
    tempB = sensorB.readTempC() # read from sensor B
    
    # print both results
    print("A:" + str(tempA) + "    " "B:" + str(tempB))
    
    sleep_ms(1000) # delay 1 second