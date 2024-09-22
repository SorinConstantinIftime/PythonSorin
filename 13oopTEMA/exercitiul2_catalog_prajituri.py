class CatalogPrajituri:
    def __init__(self):
        self.prajituri = []

    def adauga_prajitura(self):
        nume = input("Introduceti numele prajiturii: ")
        pret = int(input("Introduceti pretul: "))
        gramaj = int(input("Introduceti gramajul: "))
        self.prajituri.append({"nume": nume, "pret": pret, "gramaj": gramaj})

    def afiseaza_sortat(self, criteriu="nume"):

        def cheie_sortare(item):
            return item[criteriu]
        self.prajituri.sort(key=cheie_sortare)

        for prajitura in self.prajituri:
            print(f"Nume: {prajitura['nume']}, Pret: {prajitura['pret']} lei, Gramaj: {prajitura['gramaj']} g")

    def afiseaza_informatii(self):
        pass


catalog = CatalogPrajituri()

while True:
    catalog.adauga_prajitura()
    continua = input("Doresti sa adaugi alta prajitura? (da/nu): ")
    if continua.lower() != "da":
        break


class Tort(CatalogPrajituri):
    def __init__(self, nume, pret, gramaj, etajat=False, glazura=str("ciocolata")):
        super().__init__()
        self.etajat = etajat
        self.glazura = glazura

    def set_etajat(self, etajat):
        self.etajat = etajat

    def get_etajat(self):
        return self.etajat

    def set_glazura(self, glazura):
        self.glazura = glazura

    def get_glazura(self):
        return self.glazura

    def afiseaza_informatii(self):
        super().afiseaza_informatii()
        print(f"Etajat: {self.etajat}, Glazura: {self.glazura}")


class Fursec(CatalogPrajituri):
    pass


print("\nPrajiturile sortate dupa nume:")
catalog.afiseaza_sortat()

print("\nPrajiturile sortate dupa pret:")
catalog.afiseaza_sortat(criteriu="pret")

print("\nPrajiturile sortate dupa gramaj:")
catalog.afiseaza_sortat(criteriu="gramaj")



