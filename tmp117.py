# A simple class to read temperature from the TMP117 i2c temperature sensor
# Currently only supports reading temperature in C, F, K. Does not support
# alarms.

# This module has been tested with the following development boards:
#    • BBC Micro:bit
#    • Raspberry Pi Pico (RP2040)


# No warranties express or implied, including any warranty of merchantability and warranty of fitness for a particular purpose.
# Written by Michael Ruppe at Core Electronics MAR 2021

import os
_SYSNAME = os.uname().sysname

if _SYSNAME == 'microbit':
    from microbit import i2c
else: # for Raspberry Pi Pico
    from machine import I2C
    i2c = I2C(0)
        
# Register definitions
REG_TEMPC = b'\x00'

class tmp117(object):    
    def __init__(self, addr_=0x48, i2c_=i2c):
        self.i2c = i2c_
        self.addr = addr_
        
        if _SYSNAME == 'microbit':
            self.i2cWrite = self.i2c.write
            self.i2cRead = self.i2c.read
        else:
            self.i2cWrite = self.i2c.writeto
            self.i2cRead = self.i2c.readfrom
    
    def readTempC(self):
        self.i2cWrite(self.addr, REG_TEMPC)
        data = self.i2cRead(self.addr, 2) # returns a bytes object
        tempDataRaw = int.from_bytes(data, 'big')
        # handle negatives (MicroPython int.from_bytes does not support signed conversion (yet)
        if tempDataRaw >= 0x8000:
            return -256.0 + (tempDataRaw - 0x8000) * 7.8125e-3 # One LSB equals 7.812 mdegC
        else:
            return tempDataRaw * 7.8125e-3 # One LSB equals 7.812 mdegC
    
    def readTempF(self):
        return (self.readTempC() * 9/5) + 32
        
    def readTempK(self):
        return self.readTempC() + 273.15
