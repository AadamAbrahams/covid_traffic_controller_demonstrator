from OmlaxTCP import motionSensor
from OmlaxTCP import tempSensor

def main():
	motionSensor.setup(0)
	motionSensor.setup(1)
	tempSensor.setup(1, 0x0a, 8)
	while True:
		tempSensor.feverScanner()
		motionSensor.direc_detect(0, 1)

if __name__ == "__main__":
	main()
