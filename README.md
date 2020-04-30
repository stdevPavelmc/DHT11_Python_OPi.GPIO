# DHT11 Python library tuned to be used with the OPi.GPIO lib for Orange Pi SBC

This simple class can be used for reading temperature and humidity values from DHT11 sensor on any of the supported SBC that works with the Orange Pi Boards and OPi.GPIO lib 

# Installation

To install, clone the repository, cd into it, and run:

```
python3 -m pip install .
```

# Usage

1. Instantiate the `DHT11` class with the pin number as constructor parameter.
2. Call `read()` method, which will return `DHT11Result` object with actual values and error code.

For example:

```python
import OPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setboard(GPIO.PRIME)    # Select Orange Pi PC board to use
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
```

For working example, see `dht11_example.py` (you probably need to adjust pin for your configuration)


# License

This project is licensed under the terms of the MIT license.

# Retribution

This lib is based on the lib by [@szazo on github](https://github.com/szazo/DHT11_Python.git) and adapted to work with the OPi.GPIO lib
