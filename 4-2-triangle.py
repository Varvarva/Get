import RPi.GPIO as gp
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

T = float(input("Введите период треугольного сигнала "))

try:
    while 1:
        for i in range(256):
            gp.output(dac, dec2bin(i))
            time.sleep(T/510)
        for i in range(254, -1, -1):
            gp.output(dac, dec2bin(i))
            time.sleep(T/510)
finally:
    gp.cleanup()