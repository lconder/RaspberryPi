import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

GPIO.setup(24, GPIO.IN)

def blink():
	GPIO.output(23, False)
	while True:
                if GPIO.input(24):
                        GPIO.output(23, True)
                         print("sound")
		else:
                        GPIO.output(23, False)

                if GPIO.input(17):
                        print("sound")
                else:
                        print("not sound")
		
        
	GPIO.cleanup()
        

blink()
