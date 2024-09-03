'''
Scrie o functie care sa imparta o lista in doua liste in functie de un prag dat de la tastatura: una cu elemente
mai mici si alta cu elemente mai mari sau egale cu acel prag
Exemplu de Input si Output:

Input:
list_example = [5,2,9,1,5,6], threshold = 5

Output:
result = ([2,1], [5,9,5,6])
'''

def imparti_lista(lista, prag):

  lista_mici = []
  lista_mari = []
  for numar in lista:
    if numar < prag:
      lista_mici.append(numar)
    else:
      lista_mari.append(numar)

  return lista_mici, lista_mari


list_example = [5, 2, 9, 1, 5, 6]
prag = int(input("Introduceți pragul: "))
result = imparti_lista(list_example, prag)
print(result)