from OmlaxTCP import motionSensor
from OmlaxTCP import tempSensor


def setup():
    """
    Configures two PIR motion sensors and a temperature sensor.
    """
    motionSensor.setup(0)
    # Set up PIR sensor on GPIO pin 0.
    motionSensor.setup(1)
    # Set up PIR sensor on GPIO pin 1.
    tempSensor.setup(1, 0x0a, 8)
    # Establishes I2C communication between temperature sensor and RPi,
    # on channel 1 of the pi.


def main():
    """
    Determine if an individual stands infront of the temperature sensor,
    and if so this data is sent to the server via a TCP protocol message.
    Determines whether an individual is entering or leaving a building.
    """
    while True:
        tempSensor.feverScanner()
        # Temperature check.
        motionSensor.direc_detect(0, 1)
        # Direction detection check.


if __name__ == "__main__":
    setup()
    main()
