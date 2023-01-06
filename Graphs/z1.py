import matplotlib.pyplot as plt
from numpy import *

r = 2
t = arange(0,2*pi,.01)

x = r*sin(t)
y = r*cos(t)

z = 1
b = 1

n =-1
m=1

h=0
j =0

smile1 = linspace(-1, 1, 20)
smile2 = sin(2*smile1-pi/2)/1.5-0.2773

plt.plot(x,y,'r',label = "lamane")
plt.plot(z,b,'bo', label = "punkty")
plt.plot(n,m,'bo')
plt.plot(h,j,'bo')
plt.plot(smile1,smile2,'y', label = "sinus")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Current mood")
plt.legend()
plt.show()