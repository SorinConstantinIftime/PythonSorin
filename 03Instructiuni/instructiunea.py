# my_var = 5
# if my_var:
#     print("set instructiuni 1")

# my_var = None
# if my_var:
#     print("set instructiuni 1")
# else:
#     print("set instructiuni 2")

# my_var = 5
#
# if my_var < 6 :
#         print("set instructiuni 1")
# else:
#         print("set instructiuni 2")


# my_var = 5
# if my_var > 6 :
#         print("set instructiuni 1")
# elif my_var > 8:
#     print("set instructiuni 2")
# elif my_var <= 5:
#     print("set instructiuni 3")
# else:
#         print("set instructiuni 4")

#salariu, nivel_salariu = 2, None
# nivel_salariu = None
# salariu = 2
# if salariu > 4:
#     print("salariu mare")
# elif salariu == 3:
#     print("salariu mediu")
# else:
#     print("salariu mare")

# nivel_salariu ="salariu mic"
#salariu = 2
# if salariu > 4:
#     nivel_salariu = "salariu mare"
# elif salariu == 3:
#     nivel_salariu ="salariu mediu"
# print(nivel_salariu)

# salariu = 2
# nivel_salariu = "salariul este mare" if salariu > 4 else "salariul este mic"
# print(nivel_salariu)

salariu_brut = None
salariu = 3
nivel_salariu = "salariul este ok"
if (salariu_net := salariu + 2) and salariu_net > 4 and (salariu_brut:= salariu_net - 2):
    nivel_salariu = f"salariu este maresi are valoarea {salariu_brut}"
elif (salariu_net := salariu + 1) and salariu_net >= 3 :
    nivel_salariu = "salariu este mediu"
print(nivel_salariu)
print(salariu_brut)






