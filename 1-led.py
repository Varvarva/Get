import RPi.GPIO as GPIO

leds = [2,3,4,17,27,22,10,9]
AUX = [21,20,26,16,19,25,23,24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(AUX,GPIO.IN)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,0)

while True:
     for i in range(len(AUX)):
        GPIO.output(leds[i], GPIO.input(AUX[i]))

GPIO.cleanup()
