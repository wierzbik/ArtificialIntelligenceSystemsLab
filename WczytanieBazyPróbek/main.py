from tabulate import tabulate
def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami,
                                  nazwa_pliku_z_opisem_atr):
    try:
        with open(nazwa_pliku_z_wartosciami, "r") as f:
            wartosci = f.read()
    except:
        print("Błąd odczytu pliku z wartościami")
        return None, None, None
    try:
        with open(nazwa_pliku_z_opisem_atr, "r") as f:
            opis = f.read()
    except:
        print("Błąd odczytu pliku z opisem atrybutów")
        return None, None, None

    probki = []
    czy_atr_symb = []
    nazwy_atr = []

    wartosci = wartosci.split("\n")
    opis = opis.split("\n")

    for linia in wartosci:
        probki.append(linia.split())

    for linia in opis:
        tmp = linia.split()
        nazwy_atr.append(tmp[0])
        if tmp[1] == "s":
            czy_atr_symb.append(True)
        else:
            czy_atr_symb.append(False)


    return probki, czy_atr_symb, nazwy_atr

p, c, n = wczytaj_baze_probek_z_tekstem("wartości.txt", "opis.txt")

tab = []
for i in range(len(p)):
    if p[i][4] == '1':
        p[i][4] = 'Setosa'
    elif p[i][4] == '2':
        p[i][4] = 'Versicolour'
    else:
        p[i][4] = 'Virginica'
print(tabulate(p,n, tablefmt="fancy_grid"))

for i in range(len(c)):
    tab.append([n[i],c[i]])
a = ["Nazwa","Czy_atr_symb"]
print(tabulate(tab,a,tablefmt="fancy_grid"))
