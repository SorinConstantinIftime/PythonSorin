'''
Scrie o functie care sa enumere cate elemente pozitive sunt intr-un tuplu dat.
Exemplu de Input si Output
Input:
tuple_example = (-1,3,-2,4,0)
Output:
result = 2 (deoarece sunt 2 numere pozitive: 3 si 4)
'''

def tuplu_pozitiv(my_tuple):
    contor = 0
    for numar_pozitiv in my_tuple:
        if numar_pozitiv > 0:
            contor = contor + 1

    return contor


my_tuple = (-1, 3, -2, 4, 0)
rezultat = tuplu_pozitiv(my_tuple)
print(rezultat)