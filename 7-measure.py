import RPi.GPIO as gp
import time
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [2, 3, 4, 17, 27, 22, 10, 9]

gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
gp.setup(leds, gp.OUT)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
gp.setup(comp, gp.IN)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

#функция, измеряющая напряжение на тройке
def troyka_measure():
    val = 0
    for i in range(7, -1, -1):
        gp.output(dac, dec2bin(val+2**i))
        time.sleep(0.001)
        if (gp.input(comp) == 0):
            val += 2**i
    return val

#функция вывода числа на светодиоды
def bin2leds(n):
    gp.output(leds, dec2bin(n))

try:
    measurments = []
    timeline = []
    t_start = time.time()
    gp.output(troyka, 1) #начало зарядки
    cur_m = troyka_measure()
    measurments.append(cur_m/256*3.3)
    print(cur_m/256*3.3)
    bin2leds(cur_m)
    while measurments[-1] < 3.19:
        cur_m = troyka_measure()
        measurments.append(cur_m/256*3.3)
        print(cur_m/256*3.3)
        bin2leds(cur_m)
    gp.output(troyka, 0) #начало разрядки
    while measurments[-1] > 0.2:
        cur_m = troyka_measure()
        measurments.append(cur_m/256*3.3)
        print(cur_m/256*3.3)
        bin2leds(cur_m)
    t_finish = time.time()
    #обработка данных
    plt.plot(measurments)
    plt.show()
    duration = t_finish-t_start
    print('\nSettings:')
    print(duration)
    with open('data.txt', 'w') as f:
        for el in measurments:
            f.write(str(el))
            f.write('\n')
    with open('settings.txt', 'w') as f:
        f.write('Частота дискретизации: ')
        f.write(str(len(measurments)/duration))
        f.write('Гц\nШаг квантования: ')
        f.write(str(3.3/256))
        f.write('В')
    print(duration/len(measurments))
    print(len(measurments)/duration)
    print(3.3/256)
finally:

    gp.cleanup()