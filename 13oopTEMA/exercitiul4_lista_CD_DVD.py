class lista_CD_DVD:
    def __init__(self, titlu, continut):
        self.titlu = titlu
        self.continut = continut
        global lista_obiecte
        try:
            lista_obiecte.append(self)
        except NameError:
            lista_obiecte = [self]

    def __str__(self):
        return self.titlu

    @staticmethod
    def cauta(text):
        for obiect in lista_obiecte:
            if text in obiect.titlu or text in obiect.continut:
                print(f"Am găsit: \n{obiect}")

# Creare obiecte
cd1 = lista_CD_DVD("Best of Rock", "Colecție de hituri rock")
dvd1 = lista_CD_DVD("Lord of the Rings", "Trilogie fantasy")
carte1 = lista_CD_DVD("Python pentru începători", "Tutorial Python")  # Exemplu de obiect incorect

# Căutare pozitivă
lista_CD_DVD.cauta("Lord")

# Căutare negativă
lista_CD_DVD.cauta("Java")

# Afisare toate obiectele
for obiect in lista_obiecte:
    print(obiect)