import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN)

def blink():
	GPIO.output(17, False)
	while True:
                if GPIO.input(27):
                        GPIO.output(17, True)
                        
                        
		else:
                        print ("pressed")
                        GPIO.output(17, False)
                
		
        
	GPIO.cleanup()
        

blink()
