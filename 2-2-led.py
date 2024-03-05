import RPi.GPIO as GPIO
import time
dac=[8,11,7,1,0,5,12,6]
num=[1,1,1,1,1,1,1,1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
for i in range(8):
    GPIO.output(dac[i],num[i])
time.sleep(15)
GPIO.output(dac,0)
GPIO.cleanup()
