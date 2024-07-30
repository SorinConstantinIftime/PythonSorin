'''
sa se acceseze un element dintr-o lista dupa indexul specificat de utilizator.
folosim try except pentru a gestiuna lipsa unui index din lista
'''
lista = [1, 2, 3, 4, 5]
try:
    valoare_index = int(input('Introduceti indexul:'))
    print(lista[valoare_index])
except IndexError:
    print('indexul este in afara limitelor listei')
    while valoare_index > len(lista) - 1:
        valoare_index = int(input('Introduceti indexul:'))
    print(lista[valoare_index])

