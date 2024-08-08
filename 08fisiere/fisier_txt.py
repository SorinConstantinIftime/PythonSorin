'''
r -> citire, nu adauga, este valoare default, daca fisierul nu exista apare eroare
w -> scrire, daca fisierul nu exista, il adauga, daca exista info in fisiere, este rescrisa
a -> scriere, daca exista informatie in fisier, adauga, nu rescrie
\n - new line

r+ -> screiere, citire, fisierul nu exista, apare eroare
'''


# file = open('data.txt', 'r+')
# file.write('hello\n')
# file.close()
#
# file = open('data.txt', 'a')
# file.write('hello1\n')
# file.close()

# with open('data.txt', 'w') as file:
#     file.write('hello')

# with open('data.txt', 'r') as file:
#     test = file.readlines()
#     print(test)
#     for line in test:
#         print(line)

# with open('data.txt', 'r') as file:
#     # print(list(file))
#     for line in (list(file)):
#         print(line)

with open('data.txt', 'r') as unicorn:
    while True:
        line = unicorn.readline()
        if not line:
            break
        print(line)