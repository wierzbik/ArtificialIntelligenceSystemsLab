def  probki_str_na_liczby (probki_str, numery_atr):
    probki_num = []
    list1 = []
    list2 = []
    try:
        if len(probki_str[0]) == len(probki_str[1]):
            for i in range(len(probki)):
                for j in (numery_atr):
                    probki_num.append(float(probki_str[i][j]))
            dlugosc = len(probki_num) / len(numery_atr)
            tmp = 0
            for j in probki_num:
                if dlugosc > tmp:
                    list1.append(j)
                    tmp = tmp + 1
                else:
                    list2.append(j)
                    tmp = tmp + 1
            calosc = [list1] + [list2]
            return calosc
        else:
            print("Rozne dlugosci wierszy - blad")
    except:
        print("Bledny typ danych ")
        return

probki = [[1, 'a', 2.2], [3, '4', 5]]
numery_atr = [0, 2]
x = probki_str_na_liczby(probki,numery_atr)
print(x)
