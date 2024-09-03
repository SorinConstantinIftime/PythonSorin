import random


def tabela_joc(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def verifica_castigator(tabla_joc):
    for i in range(3):
        if tabla_joc[i][0] == tabla_joc[i][1] == tabla_joc[i][2] != ' ':
            return tabla_joc[i][0]
        if tabla_joc[0][i] == tabla_joc[1][i] == tabla_joc[2][i] != ' ':
            return tabla_joc[0][i]
    if tabla_joc[0][0] == tabla_joc[1][1] == tabla_joc[2][2] != ' ':
        return tabla_joc[0][0]
    if tabla_joc[0][2] == tabla_joc[1][1] == tabla_joc[2][0] != ' ':
        return tabla_joc[0][2]
    return None


def tabela_plina(tabla_joc):
    return all(cell != ' ' for row in tabla_joc for cell in row)


def gaseste_spatii(tabla_joc):
    return [(r, c) for r in range(3) for c in range(3) if tabla_joc[r][c] == ' ']


def mutare_jucator(tabla_joc):
    while True:
        try:
            row, col = map(int, input("Introduceți mișcarea (rand si coloana): ").split())
            if tabla_joc[row][col] != ' ':
                print("Celula este deja ocupată. Alegeți altceva.")
                continue
            tabla_joc[row][col] = 'X'
            break
        except (ValueError, IndexError):
            print("Input invalid. Introduceți rând și coloană ca două numere separate prin spațiu (0, 1 sau 2).")


def alegere_calculator(tabla_joc):
    row, col = random.choice(gaseste_spatii(tabla_joc))
    tabla_joc[row][col] = '0'
    print(f"Calculatorul a ales mișcarea: ({row}, {col})")


def xsi0():
    tabla_joc = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        tabela_joc(tabla_joc)
        mutare_jucator(tabla_joc)

        if verifica_castigator(tabla_joc) == 'X':
            tabela_joc(tabla_joc)
            print("Felicitări! Ați câștigat!")
            break
        if tabela_plina(tabla_joc):
            tabela_joc(tabla_joc)
            print("Egalitate!")
            break

        alegere_calculator(tabla_joc)

        if verifica_castigator(tabla_joc) == '0':
            tabela_joc(tabla_joc)
            print("Calculatorul a câștigat.")
            break
        if tabela_plina(tabla_joc):
            tabela_joc(tabla_joc)
            print("Egalitate!")
            break


# if __name__ == "__main__":
#     xsi0()