import csv
import os
from operator import itemgetter


def csv_reader(file_name):
    lista_elemente = []
    with open(file_name, 'r') as file:
        categorii = csv.reader(file)
        for item in categorii:
            lista_elemente.append(item)
    return lista_elemente


print('Sterge fișierele --categoriiposibile.csv-- și --tasks.csv-- înainte de a începe')

i = 0

while i < 4:
    with open('categoriiposibile.csv', mode='a', newline='') as file:
        lista_elemente = csv_reader('categoriiposibile.csv')
        print(lista_elemente)
        variabila_categorie = input('Adaugă un nou element (muncă/cadouri/curs/cumpărături): ')
        lista_elemente_noi = [i[0] for i in lista_elemente]
        if variabila_categorie not in lista_elemente_noi:
            writer = csv.writer(file)
            writer.writerow([variabila_categorie])
            i += 1
        else:
            print('Elementul există deja, încearcă din nou.')
        lista_elemente_noi2 = [i[0] for i in lista_elemente]

categories = ('curs', 'cumpărături', 'muncă', 'cadouri')
tasks = ('Nume_task', 'Deadline', 'Responsabil', 'Categorie')


def csv_reader2():
    lista_elemente_taskuri = ['Nume_task', 'Deadline', 'Responsabil', 'Categorie']
    print(lista_elemente_taskuri)
    with open('tasks.csv', 'r+') as file:
        lista_taskuri = csv.reader(file)
        for item in lista_taskuri:
            lista_elemente_taskuri.append(item)
    return lista_elemente_taskuri


j = 0
while j < 4:
    with open('tasks.csv', 'a', newline='') as csv_file:
        lista_elemente_taskuri = csv_reader2()
        new_task_name = input('Adaugă un nou task: ')
        new_task_deadline = input('Adaugă un deadline pentru noul task de format ZZ.LL.AAAA: ')
        new_task_responsabil = input('Adaugă un responsabil pentru noul task: ')
        new_task_categorie = input(f'Adaugă o categorie pentru noul task, din cele existente: ')

        if new_task_categorie in [i[0] for i in csv_reader('categoriiposibile.csv')]:
            writer = csv.writer(csv_file)

            # dacă fișierul este gol, adăugăm headerul
            if os.path.getsize('tasks.csv') == 0:
                writer.writerow(tasks)

            writer.writerow([new_task_name, new_task_deadline, new_task_responsabil, new_task_categorie])
            j += 1
        else:
            print('Categoria aleasă nu există.')

# adăugare date în fișierul nostru CSV într-un dicționar și apoi sortare
header_table = []
with open('tasks.csv', mode='r', newline='') as f:
    # citim tot conținutul fișierului folosind metoda readlines()
    lines_read = f.readlines()
    print(lines_read)
    if len(lines_read) == 0:
        exit('Fișierul CSV este gol. Oprire.')

    # inițializăm o listă de dicționare, fiecare rând citit din fișier va deveni un dicționar
    all_lines_list_of_dicts = []

    # luăm headerul tabelului (linia 0) și apoi citim fișierul linie cu linie
    for idx, line in enumerate(lines_read):
        if idx == 0:
            # ia primul rând din CSV, înlătură newline, apoi separă prin virgulă
            header_table = [key for key in line.replace("\n", "").split(",")]
        else:
            a_line_as_dict = {}
            tokenes_line = line.replace("\n", "").split(",")
            # iterăm de câte ori sunt coloane în CSV și populăm dicționarul
            for jdx in range(len(header_table)):
                a_line_as_dict[header_table[jdx]] = tokenes_line[jdx]
            all_lines_list_of_dicts.append(a_line_as_dict)

    print(all_lines_list_of_dicts)

    # alegem cheia de sortare după index
    idx_selector_key_sorted = int(input(f"Alege indexul (indexul începe de la 0) unei chei pentru sortare: "))

    # folosim sorted din Python pentru sortarea colecțiilor
    newlist = sorted(all_lines_list_of_dicts, key=itemgetter(header_table[idx_selector_key_sorted]))

    print(f"### Sortat după: {header_table[idx_selector_key_sorted]} ###")
    print(newlist)
