'''
1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
preluat automat de la tastatura.
'''
# text_utilizator = input('Introduceti text: ')
# variabila_test_string = True
# for i in text_utilizator:
#     if i in ("0123456789"):
#         variabila_test_string = False
#         break
# # print(variabila_test_string)
# if variabila_test_string is False:
#     print("este numar")
# else:
#     print("este string")
######################################################
'''
# 2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
# numar este par sau impar si afisati un raspuns in acest sens.
# '''
# cifra = int(input('introduceti cifra: '))
# if cifra % 2 == 0:
#     print('este par')
# else:
#     print("este inpar")
#########################################
'''
# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
# la 4 (fara rest)
# '''
# cifra = int(input('introduceti an: '))
# if cifra % 4 == 0:
#     print('An bisect')
# else:
#     print("Anul nu este bisect")
################################################################
'''
# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
# afisati numarul pozitiv.
# '''
# cifra = int(input('introduceti numar: '))
# if cifra > 0:
#     print('numarul este pozitiv')
#     if cifra < 10:
#         print('numar mai mic decat 10')
# elif cifra < 0:
#     cifra = cifra * (-1)
#     print(cifra)
#     print('numar negativ')
# else:
#     print('numar este 0')
#
#####################################
'''
5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
acest sir de caractere:
“”” 1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi “””
Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
'''
# cifra = input('introduceti numarul din meniu: ')
# lista_cumparaturi = ['suc', 'apa']
# if cifra == "1":
#     print("Afisare lista de cumparaturi")
# elif cifra == "2":
#     adaugare_element = input("Adaugare element: ")
#     lista_cumparaturi.append(adaugare_element)
#     print(lista_cumparaturi)
# elif cifra == "3":
#     print(lista_cumparaturi)
#     stergere_element = input('Stergere element')
#     if stergere_element in lista_cumparaturi:
#         lista_cumparaturi.remove((stergere_element))
#         print(lista_cumparaturi)
# elif cifra == "4":
#     print("Sterere lista de cumparaturi")
#     lista_cumparaturi.clear()
#     print(lista_cumparaturi)
# elif cifra == "5":
#     print("Cautare in lista de cumparaturi")
#     cautare_element = input('Introdu un element: ')
#     if cautare_element in lista_cumparaturi:
#         print('Elementul exista')
#     else:
#         print('Elementul nu exista')
#
# else:
#     print("Alegerea nu exista. Reincercati")
# #####################################################

# variabila_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# variabila_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# variabila_comuna = []
# for numar in variabila_a:
#   if numar in variabila_b and numar not in variabila_comuna:
#     variabila_comuna.append(numar)
# print(variabila_comuna)

# variabila_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# variabila_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# variabila_comuna = []
#
# for i in variabila_a:
#     if i in variabila_b:
#         variabila_comuna.append(i)
# print(variabila_comuna)

# variabila_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# variabila_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# # print(set(variabila_a).intersection(set(variabila_b)))
# print(list(set(variabila_a).intersection(set(variabila_b))))

#############################
# TOP FILME

lista_filme = [
    {
        'nume': 'George',
        'filme': ['a', 'b', 'c']
    },
    {
        'nume': 'Cristian',
        'filme': ['b', 'c', 'd', 'e', 'a']

    },
    {
        'nume': 'Stefan',
        'filme': ['c', 'a', 'a']
    }
]
filme_vizionate = {}

cel_mai_vizionat_film = []
numar_vizionari = 0
for utilizator in lista_filme:
    for film in utilizator['filme']:
        if film in filme_vizionate:
            filme_vizionate[film] = filme_vizionate[film] + 1
            #filme_vizionate += 1
        else:
            filme_vizionate[film] = 1
        if numar_vizionari < filme_vizionate[film]:
            numar_vizionari = filme_vizionate[film]
            if film not in cel_mai_vizionat_film:
                cel_mai_vizionat_film.append(film)
            for i in cel_mai_vizionat_film:
                if filme_vizionate[i] < numar_vizionari:
                    cel_mai_vizionat_film.remove(i)
                print(i)
print(filme_vizionate)
print(numar_vizionari)
print('cel_mai_vizionat_film', cel_mai_vizionat_film)
