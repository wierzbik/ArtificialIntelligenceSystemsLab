import matplotlib.pyplot as plt
import math
import random

def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami,
                                  nazwa_pliku_z_opisem_atr):
    try:
        with open(nazwa_pliku_z_wartosciami, "r") as f:
            wartosci = f.read()
    except:
        print("Nie mozna odczytac pliku z wartosciami!")
        return None, None, None
    try:
        with open(nazwa_pliku_z_opisem_atr, "r") as f:
            opis = f.read()
    except:
        print("Nie mozna odczytac pliku z opisem atrybutow!")
        return None, None, None
    wartosci = wartosci.split("\n")
    w1 = []
    for i in wartosci:
        w1.append(i.split())
    return w1, opis

x, y = wczytaj_baze_probek_z_tekstem("spiralka.txt", 'spiralka-names.txt')

k1 = []
k2 = []

for i in range(len(x)):
    k1.append(float(x[i][0]))
    k2.append(float(x[i][1]))

def odleglosc(x1, x2, y1, y2):
    wzor = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return wzor

def centroidy(ilosc):
    srodki = []
    for i in range(ilosc):
        srodki.append([random.uniform(-1.5, 1.5), random.uniform(-1.5, 2)])
    return srodki

iteracje = 5
wspolrzedne = centroidy(7)

for i in range(len(wspolrzedne)):
    plt.plot(wspolrzedne[i][0], wspolrzedne[i][1], 'or')

tab = []
for i in range(len(wspolrzedne)):
    tab.append([])
for i in range(len(k1)):
    tmp = 1000
    nr_wiersza = 0
    for j in range(len(wspolrzedne)):
        dlugosc = odleglosc(k1[i], wspolrzedne[j][0], k2[i], wspolrzedne[j][1])
        if dlugosc < tmp:
            nr_wiersza = j
            tmp = dlugosc
    tab[nr_wiersza].append([k1[i], k2[i]])

for o in range(iteracje):
    punkty = []
    for i in range(len(wspolrzedne)):
        nowe_x1 = []
        nowe_y1 = []
        for k in range(len(tab[i])):
            nowe_x1.append(float(tab[i][k][0]))
            nowe_y1.append(float(tab[i][k][1]))
        nx3 = 0
        ny3 = 0
        for l in nowe_x1:
            nx3 = nx3 + l
        for p in nowe_y1:
            ny3 = ny3 + p
        nx3 = nx3 / len(nowe_x1)
        ny3 = ny3 / len(nowe_y1)
        punkty.append([nx3, ny3])
    tab = []
    for i in range(len(wspolrzedne)):
        tab.append([])
    for i in range(len(k1)):
        tmp = 1000
        nr_wiersza = 0
        for j in range(len(wspolrzedne)):
            dlugosc = odleglosc(k1[i], punkty[j][0], k2[i], punkty[j][1])
            if dlugosc < tmp:
                nr_wiersza = j
                tmp = dlugosc
        tab[nr_wiersza].append([k1[i], k2[i]])
    nowe_x = []
    nowe_y = []
    for i in range(len(wspolrzedne)):
        nowe_x.append([])
        nowe_y.append([])
    temp2 = 0
    for j in range(len(tab)):
        for i in range(len(tab[j])):
            nowe_x[temp2].append(float(tab[j][i][0]))
            nowe_y[temp2].append(float(tab[j][i][1]))
        temp2 = temp2 + 1
    plt.subplot(211)
    plt.title("Startowe środki")
    for i in range(len(wspolrzedne)):
        plt.plot(wspolrzedne[i][0], wspolrzedne[i][1], 'kD')

    plt.plot(k1, k2, '.', label  = "Próbki")
    plt.legend()
    plt.xlabel("X")
    plt.ylabel('Y')
    plt.subplot(212)
    plt.title("Nowe środki")
    plt.xlabel("X")
    plt.ylabel('Y')
    for i in range(len(punkty)):
        plt.plot(punkty[i][0], punkty[i][1], 'kD')
    for i in range(len(tab)):
        plt.plot(nowe_x[i], nowe_y[i], '.', label = "Grupa: %i" %(i +1))
    plt.legend()
    plt.show()