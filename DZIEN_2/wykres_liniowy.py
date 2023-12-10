import numpy as np
import matplotlib.pyplot as plt

#przygotowanie danych
t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2*np.pi*t)

#przygotowanie wykresu
fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas [s]',ylabel='napięcie prądu [mV]',title='pomiar napięcia prądu w czasie t')
ax.grid()
fig.savefig('wykresliniowy.png')
plt.show()
