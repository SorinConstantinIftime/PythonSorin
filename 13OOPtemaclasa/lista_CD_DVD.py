"""
Creati o clasa care se numeste Lista_CD_DVD.
La crearea unui obiect ala cestei clase va solicita doua argumente reprezentand titlu si
continut cu care va crea doua atribute.
Fiecare obiect creat va fi adaugat intr-o lista din namespace-ul global. Clasa are o
metoda care cauta si gaseste pe baza textului dat ca argument un obiect, afisiand titlu
si continutul. Se va folosi lista de obiecte pentru a cauta.
La afisarea obiectului returnati utilizand metoda __str__ titlul obiectului.
Aplicati clasa pentru 3 exemple apoi folositi cautarea pe un caz pozitiv si unul
negativ. Printati cele 3 obiecte.
"""


class ListaCDDVD:
    obiect = []

    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut
        ListaCDDVD.obiect.append(self)

    def cautare_obiecte(self, text_cautat):
        obiecte_gasite = ""
        for i in ListaCDDVD.obiect:
            if text_cautat in i.titlu or text_cautat in i.continut:
                obiecte_gasite += f"Titlu: {i.titlu}, continut: {i.continut}\n"
        if obiecte_gasite == "":
            obiecte_gasite = "Nu a fost gasita nici o inregistrare"
        return obiecte_gasite

    def __str__(self):
        return f"Titlu {self.titlu}"


obiect1 = ListaCDDVD("Muzica", "Muzica pop")
obiect2 = ListaCDDVD("Filme", "Actiune")
obiect3 = ListaCDDVD("Carti", "SF")
obiect4 = ListaCDDVD("Muzica", "Muzica rock")
print(obiect1)
print(obiect2)
print(obiect3)
print(obiect3.cautare_obiecte(text_cautat="Muzica"))
print(obiect2.cautare_obiecte(text_cautat="Filme"))
print(obiect4.cautare_obiecte(text_cautat="Muzica Pop"))