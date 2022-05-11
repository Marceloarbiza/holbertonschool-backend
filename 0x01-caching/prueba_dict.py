from typing import OrderedDict


dicto = {}
lista = []

def aldict(dicto, lista, key, value):
    if key not in dicto:
        dicto[key] = 0
    else:
        dicto[key] += 1
    for i in lista:
        if i == key:
            lista.remove(i)
    lista.append(key)
    return dicto, lista

d, l = aldict(dicto, lista, 'b', 1)
d, l = aldict(dicto, lista,  'a', 2)
d, l = aldict(dicto, lista,  'b', 3)
d, l = aldict(dicto, lista,  'c', 4)
d, l = aldict(dicto, lista,  'a', 5)
d, l = aldict(dicto, lista,  'e', 6)
d, l = aldict(dicto, lista,  'a', 7)

print(dicto, l)

# list with the keys of the dict with min value
def min_keys(dicto):
    min_value = min(dicto.values())
    min_keys = []
    for key in dicto:
        if dicto[key] == min_value:
            min_keys.append(key)
    return min_keys

print(min_keys(dicto))


def compare_lists(lista, listb):
    for i in lista:
        if i in listb:
            return i

print(compare_lists(l, min_keys(dicto)))
            