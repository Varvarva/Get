import RPi.GPIO as gp
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]


while 1:
    try:
        n = input("Пожалуйста, введите целое число от 0 до 255 ")
        if n == 'q':
            raise ZeroDivisionError
        n = int(n)
        gp.output(dac, dec2bin(n))
        print("{:.4f}".format(3.3/255*n))
    except ZeroDivisionError:
        break
    except Exception:
        print("Неверный ввод")

gp.cleanup()
