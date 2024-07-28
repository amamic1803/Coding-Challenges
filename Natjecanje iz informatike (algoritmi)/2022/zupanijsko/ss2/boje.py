pokusaj = input()
rjesenje = input()

popis_slova = {}
for i in rjesenje:
    if i in popis_slova.keys():
        popis_slova[i] += 1
    else:
        popis_slova[i] = 1
for i in pokusaj:
    if i not in popis_slova.keys():
        popis_slova[i] = 0


ispis = []

for i in range(len(pokusaj)):
    if pokusaj[i] == rjesenje[i]:
        ispis.append("Z")
        popis_slova[pokusaj[i]] -= 1
    else:
        ispis.append("X")

for i in range(len(ispis)):
    if ispis[i] == "X":
        if popis_slova[pokusaj[i]] != 0:
            ispis[i] = "N"
            popis_slova[pokusaj[i]] -= 1
        else:
            ispis[i] = "S"

print("".join(ispis))
