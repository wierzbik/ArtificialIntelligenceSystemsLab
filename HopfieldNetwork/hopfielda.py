import numpy as np
from tkinter import *

bitmapa=[]
for i in range(5):
    wiersz = []
    for j in range(5):
        wiersz.append(0)
    bitmapa.append(wiersz)

wagi = []
for i in range(25):
    wiersz = []
    for j in range(25):
        wiersz.append(0)
    wagi.append(wiersz)
obraz_wzorcowy = []
obraz_testowy = []

def okno():
    root = Tk()
    root.title("Siec Hopfielda")
    root.geometry('550x300')

    def czarne(event):
        start_x = int(event.x / 50) * 50
        start_y = int(event.y / 50) * 50
        bitmapa[int(start_y/50)][int(start_x / 50)] = 1
        canvas.create_rectangle(start_x, start_y, start_x + 50, start_y + 50, tag='kwad',
                                fill='black')

    def biale(event):
        start_x = int(event.x / 50) * 50
        start_y = int(event.y / 50) * 50
        bitmapa[int(start_y/50)][int(start_x / 50)] = 0
        canvas.create_rectangle(start_x, start_y, start_x + 50, start_y + 50, tag='kwad1',
                                fill='white')

    canvas = Canvas(root, height=250, width=250,bg="white")
    canvas.grid(row=1, column=0,padx=5,pady=5)
    canvas.bind("<Button-1>",czarne)
    canvas.bind("<Button-3>",biale)

    canvas2=Canvas(root,height=250,width=250,bg="white")
    canvas2.grid(row=1,column=1)

    def add():
        global bitmapa
        tmp = np.reshape(bitmapa,(1,25))
        uczenie(tmp)
        bitmapa = []
        for i in range(5):
            wiersz = []
            for j in range(5):
                wiersz.append(0)
            bitmapa.append(wiersz)
        canvas.create_rectangle(0, 0, 250, 250, tag='kwad2', fill='white')

    def ucz():
        global bitmapa
        temp = np.reshape(bitmapa,(1,25))
        temp1 = temp
        for i in range(len(temp1[0])):
            if temp1[0][i] > 0:
                temp1[0][i] = 1
            else:
                temp1[0][i] = -1
        naprawa(temp1)
        a = obraz_testowy
        b = []
        for i in range(5):
            wiersz = []
            for j in range(5):
                wiersz.append(0)
            b.append(wiersz)
        tmp = 0
        for i in range(len(b)):
            for j in range(len(b[i])):
                b[i][j] = a[0][tmp]
                tmp = tmp + 1
        rys(b)

    def rys(list):
        for i in range(len(list)):
            for j in range(len(list[i])):
                if list[i][j] == 1:
                    canvas2.create_rectangle(j * 50, i * 50,
                                                                 j * 50 + 50,
                                                                 i * 50 + 50, tag='kwad3',
                                                                 fill='black')
                else:
                    canvas2.create_rectangle(j * 50, i * 50,
                                                                 j * 50 + 50,
                                                                 i * 50 + 50, tag='kwad4',
                                                                 fill='white')


    button1 = Button(root, text="Dodaj obraz wzorcowy",command=add)
    button1.grid(row=0,column=0)
    button2 = Button(root,text="Napraw",command=ucz)
    button2.grid(row=0,column=1)

    return root

def uczenie(obraz_wzorcowy):
    ob_wz = obraz_wzorcowy
    for i in range(len(ob_wz[0])):
        if ob_wz[0][i] > 0:
            ob_wz[0][i] = 1
        else:
            ob_wz[0][i] = -1
    tmp = []
    for i in range(25):
        wiersz = []
        for j in range(25):
            wiersz.append(0)
        tmp.append(wiersz)
    waga=tmp
    for i in range(len(ob_wz[0])):
        for j in range(len(ob_wz[0])):
            if i != j:
                waga[i][j] = tmp[i][j] +(1/25)* ob_wz[0][i] * ob_wz[0][j]
            wagi[i][j] = wagi[i][j]+waga[i][j]
    return waga

def naprawa(obraz_test):
    obraz = []
    for i in range(len(obraz_test[0])):
        tmp = 0
        for j in range(len(wagi[i])):
            if i != j:
                suma = obraz_test[0][j]*wagi[i][j]
                tmp = tmp+suma
        if tmp >=0:
            obraz.append(1)
        else:
            obraz.append(0)
    obraz_testowy.append(obraz)
    return obraz
if __name__ == '__main__':
    root = okno()

    root.mainloop()