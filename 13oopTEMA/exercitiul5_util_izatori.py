class EroareLungimeNepermisa(Exception):
    pass

class util:
    def __init__(self):
        self.lista_obiecte = []

class izatori:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

class utilizatori(util, izatori):
    def __init__(self, user, passw):
        izatori.__init__(self, user, passw)
        util.__init__(self)
        self.lista_obiecte.append(self)

    def __len__(self):
        raise EroareLungimeNepermisa("Nu se poate determina lungimea unui obiect de tip utilizator.")

    def parole(self):
        return {obj.passw for obj in self.lista_obiecte}

    def useri(self):
        return {obj.user for obj in self.lista_obiecte}

# Creare obiecte
user1 = utilizatori("user1", "parola1")
user2 = utilizatori("user2", "parola2")
user3 = utilizatori("user3", "parola1")

# Testare
print(user1.useri())  # Afiseaza setul cu toti userii
print(user1.parole())  # Afiseaza setul cu toate parolele

# Încercare de a obține lungimea unui obiect
try:
    print(len(user1))
except EroareLungimeNepermisa as e:
    print(e)