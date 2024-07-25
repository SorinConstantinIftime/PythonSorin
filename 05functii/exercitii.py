# functia lambda
# def suma(x, y):
#     return x + y
#
#
# a = suma(1,2)

# suma = lambda x, y: x + y
# print(suma(1, 2))

# functia map

# list_1 = [1, 3, 5, 4]
#
# list_3 = list(map(lambda x: x * 2, list_1))
# print(list_3)

#------ va afisa [2, 6, 10, 8]

# def inmultire_la_2(x):
#     return x * 2
#
#
# list_1 = [1, 3, 5, 4]
#
# # list_3 = list(map(lambda x: x * 2, list_1))
# print(list_3)

# va afisa [2, 6, 10, 8]
# ************************************************************************
# list_1 = [1, 3, 5, 4]
# def iterare(x:int) -> list:
#     lista_noua = []
#     for i in x:
#         lista_noua.append(i * 2)
#     return lista_noua
#
# a = iterare(list_1)
# print(a)

# filter-----------------
# list_1 = [1, 3, 5, 4, 8, 12]
# list_2 = list(filter(lambda x: x % 2 ==0, list_1))
# print(list_2)
#
# def filtrare(x) -> list:
#     lista_forloop = []
#     for i in x:
#         if i % 2 == 0:
#             lista_forloop.append(i)
#         return lista_forloop
#
#
# list_2 = filtrare(list_1)
# print(list_2)

# ----------------------------------------
#------ functia zip

# lista_intregi = [1, 2, 3, 4, 5]
# lista_stringuri = ('unu', 'doi', 'trei', 'patru')
# lista_float = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
#
# rezultat = list(zip(lista_intregi, lista_stringuri, lista_float))
# print(rezultat)

# -----------------------------------------
# var = 'comprehension'
# list_for_loop = []
# for caracter in var:
#     list_for_loop.append(caracter)
# print(list_for_loop)
#
# list_for_loop = [caracter for caracter in var]
#--------------------------------------------------
# nummers_list = [x for x in range(30) if x % 2 == 0]
# print(nummers_list)


# ---------------------------------
# nummers_list = []
# # for x in range(30):
# #     if x % 2 == 0:
# #         nummers_list.append(x)
# #     else:
# #         nummers_list.append(0)
#
# numbers_list = [x if x % 2 == 0 else 0 for x in range(30)]
# print(numbers_list)
# ------------------------------

# dictionar = {i: i * i for i in range(1, 11) if i % 2 == 0}
# print(dictionar)


# -------------------------
# dictionar = {i: i * i for i in range(1, 11) if i % 2 == 0}
# print(dictionar)

# -----------Sorin


# ----Alexandra cod mai jos
# functia lambda

# def suma(x, y):
#     return x + y


# a = suma(1, 2)

# suma = lambda x, y: x + y
# print(suma(1, 2))


# functia map

# def inmultire_la_2(x):
#     return x * 2

# inmultire_la_2 = lambda x: x * 2


# list_1 = [1, 5, 4, 6, 8, 11, 3, 12]

# list_3 = list(map(lambda x: x * 2, list_1))
# list_3 = list(map(inmultire_la_2, list_1))
# print(list_3)


# def iterare(x: list) -> list:
#     lista_noua = []
#     for i in x:
#         lista_noua.append(i * 2)
#     return lista_noua
#
#
# a = iterare(list_1)
# print(a)


# filter
# list_1 = [1, 5, 4, 6, 8, 11, 3, 12]

# list_2 = list(filter(lambda x: x % 2 != 0, list_1))
# print(list_2)


# def filtrare(x: list) -> list:
#     lista_forloop = []
#     for i in x:
#         if i % 2 == 0:
#             lista_forloop.append(i)
#     return lista_forloop
#
#
# list_2 = filtrare(list_1)
# print(list_2)


# zip
# lista_intregi = [1, 2, 3, 4, 5, 6]
# lista_stringuri = ('unu', 'doi', 'trei', 'patru', 'cinci', 'sase')
# lista_float = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
#
# # rezultat = list(zip(lista_intregi, lista_stringuri, lista_float))
# rezultat = 0
# for x, y in list(zip(lista_intregi, lista_float)):
#     rezultat = x * y + rezultat
# print(rezultat)

# var = 'comprehension'
# print(list(var))
# list_for_loop = []
# for caracter in var:
#     list_for_loop.append(caracter)
# print(list_for_loop)
# list_for_loop = [caracter for caracter in var]
# print(list_for_loop)

# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)
# numbers_list = [x for x in range(30) if x % 2 == 0]
# print(numbers_list)

# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)
#     else:
#         numbers_list.append(0)
# numbers_list = [x if x % 2 == 0 else 0 for x in range(30)]
# print(numbers_list)


# dictionar = {}
#
# for i in range(1, 11):
#     dictionar[i] = i * i
# dictionar = {i: i * i for i in range(1, 11) if i % 2 == 0}
dictionar = {i: i * i if i % 2 == 0 else 0 for i in range(1, 11)}
print(dictionar)


