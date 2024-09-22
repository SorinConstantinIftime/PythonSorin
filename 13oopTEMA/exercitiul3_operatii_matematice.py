class Calculator:
    def __init__(self, a=1, b=2, c=3, d=4):
        try:
            self.rezultat = ((a * (b + 3)) / c) * d
        except ZeroDivisionError:
            print("Eroare: Împărțire la zero!")
            self.rezultat = None
        except TypeError:
            print("Eroare: Tipuri de date nepotrivite!")
            self.rezultat = None

    def __str__(self):
        if self.rezultat is not None:
            return f"Rezultatul calculului este: {self.rezultat}"
        else:
            return "A apărut o eroare în timpul calculului."

# Exemple de utilizare
# 1. Cu patru parametrii numerici diferiti de cei default

calc1 = Calculator(5, 2, 4, 1)
print(calc1)

# 2. Cu 3 parametrii non-numerici
calc2 = Calculator("a", "b", "c")
print(calc2)

# 3. Cu 2 parametrii numerici
calc3 = Calculator(2, 3)
print(calc3)