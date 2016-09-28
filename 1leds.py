import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def blink():
	print( "Ejecucion iniciada")
	iteracion = 0
	while iteracion < 30:
                print(str(iteracion))
		GPIO.output(17, True)
		time.sleep(5)
		GPIO.output(17, False)
		time.sleep(10)
		iteracion = iteracion+1
	print( "Ejecucion finalizada")
	GPIO.cleanup()


blink()
