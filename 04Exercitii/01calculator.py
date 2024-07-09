# #operatii_matematice = '+-*/' #putea sa fie si set
# operator_1 = input("Primul operator: ")
# # operator_2 = float(input("Al doilea operator: "))
# # verificam daca ceeea ce introduce utilizatorul sau contine 0-9 sau  . punct
# stare_conversie = True
# for element in operator_1:
#     #print(element,'element')
#     if element in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
#         print(element, 'se afla')
#     else:
#         stare_conversie = False
#         print(element,'nu se afla')
#         break
# print(stare_conversie, 'stare conversie')
##############################################################
#operatii_matematice = '+-*/' #putea sa fie si set
# operator_1 = input("Primul operator: ")
# # operator_2 = float(input("Al doilea operator: "))
# # verificam daca ceeea ce introduce utilizatorul sau contine 0-9 sau  . punct
# stare_conversie = True
# for element in operator_1:
#     #print(element,'element')
#     if element not in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
#         stare_conversie = False
#         break
# print(stare_conversie, 'stare conversie')
# #daca putem sa convertim atunci realizam conversia
# if stare_conversie is True:
#     operator_1_convertit = float(operator_1)
# operator_2 = input("al doilea: ")
# # operator_2 = float(input("Al doilea operator: "))
# # verificam daca ceeea ce introduce utilizatorul sau contine 0-9 sau  . punct
# stare_conversie = True
# for element in operator_2:
#     #print(element,'element')
#     if element not in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
#         stare_conversie = False
#         break
# #daca putem sa convertim atunci realizam conversia
# if stare_conversie is True:
#     operator_2_convertit = float(operator_2)
# #putem efectua operatiile
# #daca operatiile se afla in stringul cautat
# operatie = input('introdu operatia dorita (+-/*')
#######################################################
# operator_1 = input("Primul operator: ")
# operator_2 = input("al doilea: ")
# operatie = input('introdu operatia dorita (+-/*): ')
# operatii_matematice = '*-+/'
# stare_conversie = True
# for element in operator_1:
#     #print(element,'element')
#     if element not in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
#         stare_conversie = False
#         break
# for element in operator_2:
#     #print(element,'element')
#     if element not in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
#         stare_conversie = False
#         break
# if stare_conversie is True:
#     operator_1_convertit = float(operator_1)
#     operator_2_convertit = float(operator_2)
#     #putem efectua operatiile
#     #daca operatiile se afla in stringul cautat
#     if len(operatie) == 1 and operatie in operatii_matematice:
#         rezultat = None
#         #daca operator este + aduci realizam adunare
#         #daca operatorul este - atunci este scadere
#         #daca operatorul este *
#         #daca operatorul este /
#         if operatie == '+':
#             rezultat = operator_1_convertit + operator_2_convertit
#         elif operatie == '-':
#             rezultat = operator_1_convertit - operator_2_convertit
#         elif operatie == '*':
#             rezultat = operator_1_convertit * operator_2_convertit
#         elif operator_2_convertit != 0.0:
#             rezultat = operator_1_convertit / operator_2_convertit
#         print(rezultat)
#######################################
operator_1 = input("Primul operator: ")
stare_conversie = True
for element in operator_1:
    #print(element,'element')
    if element not in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
        stare_conversie = False
        break
if stare_conversie is True:
    operator_2 = input("al doilea: ")

    for element in operator_2:
        #print(element,'element')
        if element not in ['0', '1,', '2', '4', '5', '6', '7', '8', '9', '.']:
            stare_conversie = False
            break
    if stare_conversie is True:
        operatie = input('introdu operatia dorita (+-/*): ')
        operator_1_convertit = float(operator_1)
        operator_2_convertit = float(operator_2)
        #putem efectua operatiile
        #daca operatiile se afla in stringul cautat
        if len(operatie) == 1 and operatie in '*-+/':
            rezultat = None
            #daca operator este + aduci realizam adunare
            #daca operatorul este - atunci este scadere
            #daca operatorul este *
            #daca operatorul este /
            if operatie == '+':
                rezultat = operator_1_convertit + operator_2_convertit
            elif operatie == '-':
                rezultat = operator_1_convertit - operator_2_convertit
            elif operatie == '*':
                rezultat = operator_1_convertit * operator_2_convertit
            elif operator_2_convertit != 0.0:
                rezultat = operator_1_convertit / operator_2_convertit
            print(f'{operator_1_convertit}{operatie}{operator_2_convertit} = {rezultat}')

