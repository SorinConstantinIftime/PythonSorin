class Util:
    lista = []

    def __init__(self):
        Util.lista.append(self)

class Izatori:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw


class Utilizatori(Util, Izatori):
    def __init__(self, user, passw):
        Util.__init__(self)
        Izatori.__init__(self, user, passw)

    def __str__(self):
        return f"Utilizatori: {self.user}"

    def __parole(self):
        set_obiecte = set()
        for i in Util.lista:
            set_obiecte.add(i.passw)
        return set_obiecte

    def __useri(self):
        set_obiecte = set()
        for i in Util.lista:
            set_obiecte.add(i.user)
        return set_obiecte

    def obtine_parole(self):
        return self.__parole()

    def obtine_utilizatori(self):
        return self.__useri()

obiect1 = Utilizatori("Dan Popescu", "abracadabra")
obiect2 = Utilizatori("Radu Ionescu", "popescu")
obiect3 = Utilizatori("Elena Ionescu", "clase")
print(obiect1)
print(obiect2)
print(obiect3)
print(obiect1.obtine_parole())
print(obiect1.obtine_utilizatori())