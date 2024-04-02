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
    for i in range(256):
        gp.output(dac, dec2bin(i))
        time.sleep(0.001)
        if (gp.input(comp) == 1):
            return i
    return 255

try:
    while 1:

        print(adc())

finally:

    gp.cleanup()