import RPi.GPIO as gp
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
gp.setup(comp, gp.IN)


def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    val = 0
    for i in range(7, -1, -1):
        gp.output(dac, dec2bin(val+2**i))
        time.sleep(0.001)
        if (gp.input(comp) == 0):
            val += 2**i
    return val

try:
    while 1:

        print(adc())

finally:
    
    gp.cleanup()