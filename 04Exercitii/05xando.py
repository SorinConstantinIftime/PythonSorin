def afisare_tabla(stare):
  """
  Afișează tabla de joc cu simbolurile X și 0.
  """
  for rand in stare:
    for element in rand:
      print(f"{element}", end=" ")
    print()

def verifica_casuta_libera(stare, pozitie):
  """
  Verifică dacă o anumită poziție de pe tablă este liberă.
  """
  return stare[pozitie // 3][pozitie % 3] == "-"

def introducere_mutare(stare, simbol):
  """
  Obține mutarea de la jucător și o plasează pe tablă.
  """
  while True:
    pozitie = int(input(f"Jucător {simbol}, introdu o poziție (1-9): "))
    if 1 <= pozitie <= 9 and verifica_casuta_libera(stare, pozitie - 1):
      stare[(pozitie - 1) // 3][(pozitie - 1) % 3] = simbol
      break
    else:
      print("Pozitie invalida. Incearca din nou.")

def verifica_castigator(stare, simbol):
  """
  Verifică dacă un jucător a câștigat jocul.
  """
  # Verificare linii și coloane
  for i in range(3):
    if stare[i][0] == stare[i][1] == stare[i][2] == simbol:
      return True
    if stare[0][i] == stare[1][i] == stare[2][i] == simbol:
      return True
  # Verificare diagonale
  if stare[0][0] == stare[1][1] == stare[2][2] == simbol:
    return True
  if stare[0][2] == stare[1][1] == stare[2][0] == simbol:
    return False

def joc_x_si_0():
  """
  Funcția principală care rulează jocul.
  """
  stare = [["-" for _ in range(3)] for _ in range(3)]
  simbol_curent = "X"

  while True:
    afisare_tabla(stare)
    introducere_mutare(stare, simbol_curent)

    if verifica_castigator(stare, simbol_curent):
      afisare_tabla(stare)
      print(f"Jucătorul {simbol_curent} a câștigat!")
      break

    if all(not verifica_casuta_libera(stare, poz) for poz in range(9)):
      afisare_tabla(stare)
      print("Remiză!")
      break

    simbol_curent = "O" if simbol_curent == "X" else "X"

joc_x_si_0()