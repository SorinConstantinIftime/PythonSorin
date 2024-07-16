# cnp= S AA LL ZZ JJ NNN C
cnp = input('Indroduceti CNP: ')
constanta_control = '279146358279'
print(cnp)
sex = cnp[0]
luni_interval = range(1, 13)
zile_interval = range(1, 32)
an_nastere = cnp[1:3]
luna_nastere = cnp[3:5]
zi_nastere = cnp[5:7]
judet = cnp[7:9]
judet_interval = range(1, 53)
indentare = 0
controlor = 0
while indentare <= 11:
    partial_controlor = int(cnp[indentare]) * int(constanta_control[indentare])
    controlor = controlor + partial_controlor
    indentare = indentare + 1
print('control : ', controlor)
NNN_interval = cnp[9:12]
C_final = cnp[12]
Control = controlor % 11
print("Control :", C_final)
print("C_final:", C_final)
print(sex)
print("An nastere: " + an_nastere)
print("Luna nastere: " + luna_nastere)
print('Zi nastere: ', zi_nastere)
print('Judet: ' + judet)
print('NNN: ' + NNN_interval)
if (sex in ('1', '2') and int(luna_nastere) in luni_interval and int(zi_nastere) in zile_interval
        and int(judet) in judet_interval and int(C_final) == int(Control)):
    print('CNP corect')
else:
    print('CNP incorect')
