from omlaxtcp import motionSensor
from omlaxtcp import tempSensor
import sys


def setup():
    """
    Configures two PIR motion sensors and a temperature sensor.
    """
    motionSensor.setup(5)
    # Set up PIR sensor on GPIO pin 5.
    motionSensor.setup(6)
    # Set up PIR sensor on GPIO pin 6.
    tempSensor.setup(1, 0x0a, 8)
    # Establishes I2C communication between temperature sensor and RPi,
    # on channel 1 of the pi.


def main():
    """
    Determine if an individual stands infront of the temperature sensor,
    and if so this data is sent to the server via a TCP protocol message.
    Determines whether an individual is entering or leaving a building.
    """
    TCP.setHostIP(sys.argv[0])
    while True:
        tempSensor.feverScanner(38)
        # Temperature check.
        motionSensor.direc_detect_with_BuzzandTemp(5, 6)
        # Direction detection check.


if __name__ == "__main__":
    setup()
    main()
