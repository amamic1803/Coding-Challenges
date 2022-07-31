#!/usr/bin/python3
import copy

# . = bijelo
# # = crno
par_boja = {".": "#",
            "#": "."}


def dobar_red(matrica):
    global stupaca
    global par_boja

    pozicija = "nema"
    brk = False
    for i in range(2):
        for j in range(stupaca):
            if matrica[i][j] != "x":
                brk = True
                pozicija = (i, j)
                break
        if brk:
            break

    if pozicija == "nema":
        return True
    else:
        mog_polozaji = []
        boja_pozicije = matrica[pozicija[0]][pozicija[1]]
        if pozicija[0] == 0 and pozicija[1] == 0:
            mog_polozaji.append((1, pozicija[1]))
            mog_polozaji.append((0, pozicija[1] + 1))
        elif pozicija[0] == 0 and pozicija[1] == stupaca - 1:
            mog_polozaji.append((1, pozicija[1]))
            mog_polozaji.append((0, pozicija[1] - 1))
        elif pozicija[0] == 0:
            mog_polozaji.append((1, pozicija[1]))
            mog_polozaji.append((0, pozicija[1] - 1))
            mog_polozaji.append((0, pozicija[1] + 1))
        elif pozicija[0] == 1 and pozicija[1] == 0:
            mog_polozaji.append((0, pozicija[1]))
            mog_polozaji.append((1, pozicija[1] + 1))
        elif pozicija[0] == 1 and pozicija[1] == stupaca - 1:
            mog_polozaji.append((0, pozicija[1]))
            mog_polozaji.append((1, pozicija[1] - 1))
        elif pozicija[0] == 1:
            mog_polozaji.append((0, pozicija[1]))
            mog_polozaji.append((1, pozicija[1] - 1))
            mog_polozaji.append((1, pozicija[1] + 1))

        izbrisano = 0
        for i in range(len(mog_polozaji)):
            if matrica[mog_polozaji[i - izbrisano][0]][mog_polozaji[i - izbrisano][1]] == "x":
                mog_polozaji.pop(i - izbrisano)
                izbrisano += 1
            elif matrica[mog_polozaji[i - izbrisano][0]][mog_polozaji[i - izbrisano][1]] != par_boja[boja_pozicije]:
                mog_polozaji.pop(i - izbrisano)
                izbrisano += 1
        postoji_kombinacija = False

        for i in mog_polozaji:
            matrica[pozicija[0]][pozicija[1]] = "x"
            matrica[i[0]][i[1]] = "x"

            if dobar_red(matrica):
                postoji_kombinacija = True
                break

            matrica[pozicija[0]][pozicija[1]] = boja_pozicije
            matrica[i[0]][i[1]] = par_boja[boja_pozicije]

        if postoji_kombinacija:
            return True
        else:
            return False


redova, stupaca = map(int, input().split())
matrica = []
for x in range(redova):
    red = []
    for i in input():
        red.append(i)
    matrica.append(red)

dobrih_redova = 0
for i in range(redova - 1):
    red_matrica = copy.deepcopy(matrica[i:i + 2])
    if dobar_red(red_matrica):
        dobrih_redova += 1

print(dobrih_redova)
