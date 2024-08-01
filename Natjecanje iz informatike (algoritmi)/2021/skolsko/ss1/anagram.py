def main():
    rijec = [x for x in input()]

    for x in rijec:
        count = rijec.count(x)
        if count - (len(rijec) - count) > 1:
            print(-1)
            return

    rijec.sort()
    izlaz_str = "-"

    while len(rijec) != 0:
        izlaz_str += rijec.pop(rijec.index(poc_abc(rijec, izlaz_str)))

    print(izlaz_str[1:])


def poc_abc(lista_1, ext):
    zadnje_slovo = ext[-1]

    temp_lista = [y for y in lista_1 if y != zadnje_slovo]
    temp_lista.sort()

    for c in temp_lista:
        count = lista_1.count(c)
        if count - (len(lista_1) - count) >= 1:
            return c

    return temp_lista[0]


if __name__ == '__main__':
    main()
