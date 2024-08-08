'''
Creează o aplicație care permite utilizatorului să
adauge articole (cu preț și cantitate) la o factură și apoi să calculeze totalul.
'''

def adaugare_articol():
    factura = []
    while True:
        optiune_utilizator = input('Alege optiune: ')
        if optiune_utilizator == "1":
            pret = float(input('Introduceti pretul: '))
            cantitate = int(input('Introdu cantitate: '))
            nume = input('Introdu nume: ')
            factura.append({'nume': nume, 'pret': pret, 'cantitate': cantitate})
        elif optiune_utilizator == '2':
            total = 0
            for articol in factura:
                total = total + articol['pret']*articol['cantitate']
            print(total)
        else:
            break
    return True
adaugare_articol()

