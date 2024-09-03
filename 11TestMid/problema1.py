'''
scrie un program care sa afiseze un dictionar care:
-un numar dat de utilizator (numar pozitiv intreg) care reprezinta numarul de chei, cu prima cheie 1.
-numarul maxim de chei admise: 15.
-valorile pentru ficare cheie reprezinta suma cumulativa a numerelor de la 1 pana la cheia respentiva (de exemplu, cheie 4 valoare 10,
deoarece 1+2+3+4=10)
exemplu input si outpput:
input - utilizatorul introduce numarul 5.
output:
dictionar :{1:1, 2:3, 3:6, 4:10, 5:10}

'''
def nr_de_chei(x: int) -> dict:
    dictionar = {}
    if x < 0:
        print("Numarul trebuie sa fie pozitiv")

    elif x < 16:
        for i in range(1, x+1):
            dictionar[i] = i * (i + 1) // 2

        return dictionar
    else:
        print("Numarul maxim este 15")


numar_utilizator = int(input("Introduceti un numar intreg pozitiv intre (1 - 15):\n"))
print(nr_de_chei(numar_utilizator))