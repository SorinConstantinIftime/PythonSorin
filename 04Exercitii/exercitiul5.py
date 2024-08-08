'''
Creează un program care convertește o sumă
dintr-o monedă în alta folosind un curs de schimb fix.
'''


def schimb():
    curs_valutar = float(input('Alegeti cursul valutar: '))
    suma = float(input('Introdu suma:'))
    valoare = suma * curs_valutar
    return valoare

schimb_valutar = schimb()
print(schimb_valutar)

