import matplotlib.pyplot as plt

def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami,
                                  nazwa_pliku_z_opisem_atr):
    try:
        with open(nazwa_pliku_z_wartosciami, "r") as f:
            wartosci = f.read()
    except:
        print("Nie można odczytać pliku z wartościami!")
        return None, None, None
    try:
        with open(nazwa_pliku_z_opisem_atr, "r") as f:
            opis = f.read()
    except:
        print("Nie można odczytać pliku z opisem atrybutów!")
        return None, None, None

    klasa1 = []
    klasa2 = []
    klasa3 = []
    tmp = []

    wartosci = wartosci.split("\n")

    for linia in wartosci:
        tmp.append(linia.split())

    for i in range(len(tmp)):
        if int(tmp[i][4]) == 1:
            klasa1.append(tmp[i])
        elif int(tmp[i][4]) == 2:
            klasa2.append(tmp[i])
        else:
            klasa3.append(tmp[i])
    return klasa1, klasa2, klasa3


k1,k2,k3=wczytaj_baze_probek_z_tekstem("iris.txt", 'iris.txt')
#print(k1)
#print(k2)
#print(k3)

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x21 = []
y21 = []
x22 = []
y22 = []
x23 = []
y23 = []
x24 = []
y24 = []
x31 = []
y31 = []
x32 = []
y32 = []
x33 = []
y33 = []
x34 = []
y34 = []

for i in range(len(k1)):
    x1.append(float(k1[i][2]))
    y1.append(float(k1[i][3]))
    x2.append(float(k1[i][1]))
    y2.append(float(k1[i][3]))
    x3.append(float(k1[i][0]))
    y3.append(float(k1[i][3]))
    x4.append(float(k1[i][1]))
    y4.append(float(k1[i][2]))

for i in range(len(k2)):
    x21.append(float(k2[i][2]))
    y21.append(float(k2[i][3]))
    x22.append(float(k2[i][1]))
    y22.append(float(k2[i][3]))
    x23.append(float(k2[i][0]))
    y23.append(float(k2[i][3]))
    x24.append(float(k2[i][1]))
    y24.append(float(k2[i][2]))

for i in range(len(k3)):
    x31.append(float(k3[i][2]))
    y31.append(float(k3[i][3]))
    x32.append(float(k3[i][1]))
    y32.append(float(k3[i][3]))
    x33.append(float(k3[i][0]))
    y33.append(float(k3[i][3]))
    x34.append(float(k3[i][1]))
    y34.append(float(k3[i][2]))


plt.subplot(2,2,1)
plt.plot(x1,y1,'b.', label = "Setosa")
plt.plot(x21,y21,'r.', label = "Versicolour")
plt.plot(x31,y31,'g.', label = "Virginica")
plt.xlabel("petal_length_in_cm")
plt.ylabel("petal_width_in_cm")
plt.legend()
plt.title("Przestrzeń 1")
plt.subplot(2,2,2)
plt.plot(x2,y2,'b.', label = "Setosa")
plt.plot(x22,y22,'r.', label = "Versicolour")
plt.plot(x32,y32,'g.', label = "Virginica")
plt.xlabel("sepal_width_in_cm")
plt.ylabel("petal_width_in_cm")
plt.legend()
plt.title("Przestrzeń 2")
plt.subplot(2,2,3)
plt.plot(x3,y3,'b.', label = "Setosa")
plt.plot(x23,y23,'r.', label = "Versicolour")
plt.plot(x33,y33,'g.', label = "Virginica")
plt.xlabel("sepal_length_in_cm")
plt.ylabel("petal_width_in_cm")
plt.legend()
plt.title("Przestrzeń 3")
plt.subplot(2,2,4)
plt.plot(x4,y4,'b.',label = "Setosa")
plt.plot(x24,y24,'r.', label = "Versicolour")
plt.plot(x34,y34,'g.',label = "Virginica")
plt.xlabel("sepal_width_in_cm")
plt.ylabel("petal_length_in_cm")
plt.legend()
plt.title("Przestrzeń 4")
plt.show()