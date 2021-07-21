# A simple class to read temperature from the TMP117 i2c temperature sensor
# Currently only supports reading temperature in C, F, K. Does not support
# alarms.

# This module has been tested with the following development boards:
#    • BBC Micro:bit
#    • Raspberry Pi Pico (RP2040)

# No warranties express or implied, including any warranty of merchantability and warranty of fitness for a particular purpose.
# Written by Michael Ruppe at Core Electronics MAR 2021
# Updated to work with unified PiicoDev i2c module.

from PiicoDev_Unified import *

# Register definitions
REG_TEMPC = b'\x00'
compat_str = 'This device library requires the latest version of the Unified PiicoDev library.  Get the latest drivers: piico.dev/unified'

class PiicoDev_TMP117(object):    
    def __init__(self, bus=None, freq=None, sda=None, scl=None, addr = 0x48):
        try:
            if compat_ind >= 1:
                self.i2c = create_unified_i2c(bus=bus, freq=freq, sda=sda, scl=scl)
                self.addr = addr
            else:
                print(compatability_string)
        except:
            print(compatability_string) 

    def readTempC(self):
        try:
            data = self.i2c.read16(self.addr, REG_TEMPC)
        except:
            print(i2c_err_str.format(self.addr))
            return None
        
        tempDataRaw = int.from_bytes(data, 'big')
        # handle negatives (MicroPython int.from_bytes does not support signed conversion (yet)
        if tempDataRaw >= 0x8000:
            return -256.0 + (tempDataRaw - 0x8000) * 7.8125e-3 # One LSB equals 7.812 mdegC
        else:
            return tempDataRaw * 7.8125e-3 # One LSB equals 7.812 mdegC
    
    def readTempF(self):
        try:
            return (self.readTempC() * 9/5) + 32
        except:
            print(i2c_err_str.format(self.addr))
            return None
        
    def readTempK(self):
        try:
            return self.readTempC() + 273.15
        except:
            print(i2c_err_str.format(self.addr))
            return None
