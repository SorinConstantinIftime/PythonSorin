# print('Mesaj')
# input('adauga un numar: ')

# def my_function(nr_mere, nume):
#     return f"{nume} are {nr_mere} mere"
#
#
# a = my_function(2, 'Ana')
# b = my_function(3, 'Maria')
# print(a)
# print(b)

def my_function(nr_mere: str, nume: str = "Ioana") -> (str, str):
    """

    :param nr_mere: numarul de mere
    :param nume: numele celui care detine merele
    :return: propozitii
    """
    return f"{nume} are {nr_mere} mere", f"{nume} are {nr_mere} pere"


a, c = my_function("2")
b, d = my_function("3", 'Maria')
e, f = my_function(nume="Gelu", nr_mere='5')
g, h = my_function(nume='Gelu')
# print(a)
# print(b)
# print(c)
# print(d)
print(g, h)

