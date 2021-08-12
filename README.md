# PiicoDev® TMP117 MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® Precision Temperature Sensor TMP117](https://core-electronics.com.au/catalog/product/view/sku/CE07502)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified).

See the Quickstart Guides for:
 - [Micro:bit](https://core-electronics.com.au/tutorials/piicodev-precision-temperature-sensor-tmp117-quickstart-guide-for-microbit.html)
 - [Raspberry Pi Pico](https://core-electronics.com.au/tutorials/piicodev-precision-temperature-sensor-tmp117-quickstart-guide-for-rpi-pico.html)
 - [Raspberry Pi](https://core-electronics.com.au/tutorials/piicodev-raspberrypi/piicodev-precision-temperature-sensor-tmp117-raspberry-pi-guide.html)

# Usage
## Example
[main.py](https://github.com/CoreElectronics/CE-PiicoDev-BME280-MicroPython-Module) is a simple example to get started.
```
from PiicoDev_TMP117 import PiicoDev_TMP117
from time import sleep
tempSensor = PiicoDev_TMP117()
while True:
    # Read and print the temperature in various units
    tempC = tempSensor.readTempC() # Celsius
    tempF = tempSensor.readTempF() # Fahrenheit
    tempK = tempSensor.readTempK() # Kelvin

    # Convert temperature into a string and print the data
    print(str(tempC) + " °C")
    sleep(1)
```
## Details
### PiicoDev_TMP117(bus=, freq=, sda=, scl=, address=0x48)
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
address | int | 0x48, 0x49, 0x4A, 0x4B | 0x48 | This address needs to match the PiicoDev Precision Temperature Sensor TMP117 hardware address configured by the jumper

### PiicoDev_TMP117.readTempC()
Parameter | Type | Unit | Description
--- | --- | --- | ---
returned | float | degC | Temperature in degrees Celsius

### PiicoDev_TMP117.readTempF()
Parameter | Type | Unit | Description
--- | --- | --- | ---
returned | float | degF| Temperature in degrees Fahrenheit

### PiicoDev_TMP117.readTempK()
Parameter | Type | Unit | Description
--- | --- | --- | ---
returned | float | K | Temperature in Kelvin

# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
