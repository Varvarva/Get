import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(21, gp.OUT)

p = gp.PWM(21, 1000)
p.start(0)

try:
    while 1:
        n = int(input("Введите коэффициент заполнения "))
        p.start(n)
        print("{:.2f}".format(3.3/100*n))
except Exception:
    print("Неверный ввод")
finally:
    gp.cleanup()