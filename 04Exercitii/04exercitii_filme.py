lista_filme = [
    {
        'nume': 'George',
        'filme': ['a', 'b', 'c']
    },
    {
        'nume': 'Cristian',
        'filme': ['b', 'c', 'd', 'e', 'a']

    },
    {
        'nume': 'Stefan',
        'filme': ['c', 'a', 'a']
    }
]
persona = None
numar_filme = 0
for i in lista_filme:
    if numar_filme < len(i['filme']):
        numar_filme = len(i['filme'])
        persona = i['nume']

print(f'{persona}: {numar_filme}')
