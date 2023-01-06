import math
from tkinter import *

list_wz = []
list_test = []
bit = []
for i in range(5):
    row = []
    for j in range(4):
        row.append(0)
    bit.append(row)

def okno():
    root = Tk()
    root.geometry('440x300')
    root.title("Algorytm zachlannego dopasowania")

    def czarne(event):
        start_x = int(event.x / 50) * 50
        start_y = int(event.y / 50) * 50
        bit[int(start_y / 50)][int(start_x / 50)] = 1
        canvas.create_rectangle(start_x, start_y, start_x + 50, start_y + 50, tag='kwad', fill='black')

    def biale(event):
        start_x = int(event.x / 50) * 50
        start_y = int(event.y / 50) * 50
        bit[int(start_y / 50)][int(start_x / 50)] = 0
        canvas.create_rectangle(start_x, start_y, start_x + 50, start_y + 50, tag='kwad1', fill='white')

    def add_list():
        global bit
        list_wz.append(bit)
        bit = []
        for i in range(5):
            dlugosc_wiersza = []
            for j in range(4):
                dlugosc_wiersza.append(0)
            bit.append(dlugosc_wiersza)
        canvas.create_rectangle(0, 0, 250, 250, tag='kwad2', fill='white')

    def prog():
        list_test.clear()
        list_test.append(bit)
        wynik = -math.inf
        for i in range(len(list_wz)):
            tmp = miara_niepodobienstwa_obustronnego(list_test[0], list_wz[i])
            if tmp >= wynik:
                wynik = tmp
                x = i
        wyn = []
        wyn.append(list_wz[x])
        for i in range(len(wyn[0])):
            for j in range(len(wyn[0][i])):
                if wyn[0][i][j] == 1:
                    canvas2.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, tag='x', fill='black')
                else:
                    canvas2.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, tag='x', fill='white')

    canvas = Canvas(root, height=250, width=200, bg="white")
    canvas.grid(row=1, column=0, padx=5, pady=5)
    canvas.bind("<Button-1>", czarne)
    canvas.bind("<Button-3>", biale)

    button_1 = Button(root, text="Dodaj obraz wzorcowy", command=add_list)
    button_1.grid(row=0, column=0)
    button_2 = Button(root, text="Znajdź najbardziej podobny obraz", command=prog)
    button_2.grid(row=0, column=1)

    canvas2 = Canvas(root, height=250, width=200, bg="white")
    canvas2.grid(row=1, column=1)

    return root


def miara_niepodobienstwa(list1, list2):
    mr = 0
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            if list1[i][j] == 1:
                odl_min = math.inf
                for k in range(len(list2)):
                    for l in range(len(list2[0])):
                        if list2[k][l] == 1:
                            odl_akt = abs(k - i) + abs(l - j)
                            odl_min = min(odl_min, odl_akt)
                mr = mr + odl_min
    return mr


def miara_niepodobienstwa_obustronnego(list1, list2):
    wynik = -(miara_niepodobienstwa(list1, list2) + miara_niepodobienstwa(list2, list1))
    return wynik


if __name__ == '__main__':
    root = okno()
    root.mainloop()