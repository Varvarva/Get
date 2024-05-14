import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.lines as mlines
import numpy as np

f = open('settings.txt', 'r')
a, b = map(float, f.read().split())
f.close()

data = np.loadtxt('data.txt', dtype=float)
data = data*b
t = []
for i in range(data.size):
    t += [i/a]
time = np.array(t)

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.set_ylabel('Напряжение, В')
ax.set_xlabel('Время, с')
ax.grid(which='major', linestyle='solid', color='grey', lw=1.2)
ax.grid(which='minor', linestyle='dashed', color='grey')
ax.set_xlim(0, time[-1])
ax.set_ylim(0, 3.3)

k = data.argmax()
t1 = time[k]
t2 = time[-1]-t1
ax.text(8.05, 2.13, f'Время заряда = {t1:.2f} с')
ax.text(8.05, 2.03, f'Время разряда = {t2:.2f} с')

ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке')
ax.plot(time, data)
ax.scatter(time[::15], data[::15])
blue_line = mlines.Line2D([], [],  marker='.',
                          markersize=10, label='V(t)')
ax.legend(handles=[blue_line])
#ax.legend(['V(t)'])
fig.savefig('graph.svg')
plt.show()