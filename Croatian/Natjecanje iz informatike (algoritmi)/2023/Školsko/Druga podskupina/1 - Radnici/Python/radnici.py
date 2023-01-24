#!/usr/bin/python3

# input
broj_radnika = int(input())
radnici = []
for x in range(broj_radnika):
    radnici.append(list(map(int, input().split())))

# trazi ono s najvise pojava (najzeljenije)
brojanje_radnih_vremena = dict()
for i in radnici:
    try:
        brojanje_radnih_vremena[f"{i[0]}-{i[1]}"] += 1
    except KeyError:
        brojanje_radnih_vremena[f"{i[0]}-{i[1]}"] = 1
najvise_pojava = max(brojanje_radnih_vremena.values())

# izdvoji ona vremena koja imaju najvise pojava (jedno ili vise ako imaju isti broj zelja)
moguca_radna_vremena = []
for i in brojanje_radnih_vremena.keys():
    if brojanje_radnih_vremena[i] == najvise_pojava:
        moguca_radna_vremena.append(i)

# pronadi koje od preostalih radnih vremena ima najkrace trajanje
moguca_radna_vremena_trajanje = []
for i in moguca_radna_vremena:
    broj1, broj2 = map(int, i.split("-"))
    moguca_radna_vremena_trajanje.append(broj2 - broj1)
najkrace = min(moguca_radna_vremena_trajanje)

# izdvoji ona vremena koja imaju isto, najkrace trajanje
preostala_moguca_vremena = []
for i in range(len(moguca_radna_vremena_trajanje)):
    if moguca_radna_vremena_trajanje[i] == najkrace:
        preostala_moguca_vremena.append(list(map(int, moguca_radna_vremena[i].split("-"))))

if len(preostala_moguca_vremena) > 1: # ako jos uvijek ima vise mogucnosti (vrijeme je imalo isti broj zelja, i isto trajanje), nadi ono koje pocinje ranije
    indeks = 0
    najranije = preostala_moguca_vremena[0][0]
    for i in range(1, len(preostala_moguca_vremena)):
        if preostala_moguca_vremena[i][0] < najranije:
            najranije = preostala_moguca_vremena[i][0]
            indeks = i
else:
    indeks = 0

# sada je poznat indeks najpozeljnijeg/najkraceg/najranijeg radnog vremena, pa ga spremimo u novu varijablu
radno_vrijeme = preostala_moguca_vremena[indeks]

# output
for i in radnici:
    if (radno_vrijeme[0] <= i[0] <= radno_vrijeme[1]) and (radno_vrijeme[0] <= i[1] <= radno_vrijeme[1]):  # ako se radnikovo zeljeno radno vrijeme nalazi u potpunosti unutar radnog vremena tvrtke, on ce raditi svoje zeljeno radno vrijeme
        print(" ".join(map(str, i)))
    else:  # ako se radnikovo zeljeno radno vrijeme nalazi izvan vremena tvrtke on ce raditi kada radi i tvrtka (radno vrijeme tvrtke)
        print(" ".join(map(str, radno_vrijeme)))

# cmd command to add extension to all files in a folder (for test-data):
# ren *.* *.*.txt
