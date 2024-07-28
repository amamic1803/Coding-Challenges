#!/usr/bin/python3

import sys


def poc_abc(lista_1, ext):
    zad_slovo = ext[-1]

    temp_lista = []
    for y in lista_1:
        if y == zad_slovo:
            pass
        else:
            temp_lista.append(y)
    temp_lista.sort()

    for a in range(len(temp_lista)):
        if lista_1.count(temp_lista[a]) - (len(lista_1) - lista_1.count(temp_lista[a])) >= 1:
            return temp_lista[a]

    return temp_lista[0]


rijec = input()
rijec_lista = []

for x in range(len(rijec)):
    rijec_lista.append(rijec[x])

izlaz = False

for x in rijec:
    if rijec.count(x) - (len(rijec) - rijec.count(x)) > 1:
        izlaz = True

if izlaz:
    print(-1)
    sys.exit()

rijec_lista_abc = rijec_lista.copy()
rijec_lista_abc.sort()

izlaz_str = "-"

obrisano = 0

while len(rijec_lista_abc) != 0:
    rijec_lista_abc.sort()

    ind = rijec_lista_abc.index(poc_abc(rijec_lista_abc, izlaz_str))
    izlaz_str += rijec_lista_abc[ind]
    del rijec_lista_abc[ind]

print(izlaz_str[1:])
# program može biti prespor za veće primjere (ovisno o brzini procesora)
