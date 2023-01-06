import numpy as np
import matplotlib.pyplot as plt
import random

def funkcja(x):
    return np.sin(x/10) * np.sin(x/200)

przedzial = np.linspace(0,100,100)
przedzial_y = funkcja(przedzial)

x = random.uniform(0,100)
y = funkcja(x)
l_iteracji = 100
wsp_przyrostu = 1.1
rozrzut = 10
plt.plot(przedzial, przedzial_y,label='sin(x/10)*sin(x/200)')
for i in range(l_iteracji):
    plt.plot(x, y, 'ro')
    x_pot = x + random.uniform(-rozrzut, rozrzut)
    if x_pot > 100:
        x_pot = 100
    elif x_pot < 0:
        x_pot = 0
    y_pot = funkcja(x_pot)
    if y_pot >= y:
        x = x_pot
        y = y_pot
        rozrzut = rozrzut * wsp_przyrostu
    elif y_pot < y:
        rozrzut = rozrzut / wsp_przyrostu
    print("Numer iteracji:",i,"x:",x,"y:", y,"rozrzut:",rozrzut)

plt.legend()
plt.title("Algorytm 1+1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()