import os
import RPi.GPIO as GPIO
import glob                                                # import glob module
import time
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

os.system('modprobe w1-gpio')                              # load one wire communication device kernel modules
os.system('modprobe w1-therm')                                                 
base_dir = '/sys/bus/w1/devices/'                          # point to the address
device_folder = glob.glob(base_dir + '28*')[0]             # find device with address starting from 28*
device_file = device_folder + '/w1_slave'

def blink():
	
                GPIO.output(23, False)
                if GPIO.input(24):
                        #GPIO.output(23, True)
                    return 1
		else:
                        #GPIO.output(23, False)
                    return 0
                
def makePost():
    payload = {'type': '0', 'hour': '12:54', 'latitude':'1', 'longitude':'1'}
    r = requests.post("http://ameca.azurewebsites.net/incident", data=payload)
    print(r.text)


def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()                                   # read the device details
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':                   # ignore first line
      time.sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')                        # find temperature in the details
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0                 # convert to Celsius
      temp_f = temp_c * 9.0 / 5.0 + 32.0                   # convert to Fahrenheit 
      return temp_c

while True:
   if (read_temp()>= 20):
       GPIO.output(23, True)
       print("temperatura sobrepasada")
       makePost()
       print(read_temp())
   else:
       GPIO.output(23, False)
       print(read_temp())
   
   
   if (blink()==1):
       GPIO.output(23, True)
       print("flama detectada")
   else:
       GPIO.output(23, False)
       print(blink())
   time.sleep(1)
  
