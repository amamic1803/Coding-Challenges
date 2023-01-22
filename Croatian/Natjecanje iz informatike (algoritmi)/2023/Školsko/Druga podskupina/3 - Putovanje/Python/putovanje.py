#!/usr/bin/python3

# funkcija koja vraca udaljenost izmedu dva grada iz upisane matrice
def vrati_udaljenost(grad1, grad2):
    global udaljenosti
    return udaljenosti[grad1][grad2]


# rekurzija
def pronadi_najmanju_udaljenost(posjeceni_gradovi, prethodni_grad):
    global broj_gradova
    global rezultati_rekurzije
    try:
        return rezultati_rekurzije[posjeceni_gradovi + str(prethodni_grad)]  # ako vec imamo rezultat za funkciju pozvanu s ovim argumentima, vratimo tu vrijednost
    except KeyError:  # ako nemamo moramo izracunati
        if posjeceni_gradovi.count("0") == 1:  # ako je ostao jos jedan grad za posjetiti (Rim) udaljenost od trenutnog grada do Rima spremimo u varijablu result
            result = vrati_udaljenost(prethodni_grad, broj_gradova - 1)

        else:  # ako ima vise neposjecenih gradova moramo provjeriti udaljenosti do svakog
            udaljenosti = []
            for i in range(1, len(posjeceni_gradovi) - 1):  # krecemo od 1 nadalje jer je jedan sigurno posjecen (odande krecemo) i stajemo prije zadnjeg jer je zadnji Rim (a njega rjesava druga grana if-a)
                if posjeceni_gradovi[i] == "0":  # ako trenutni grad nije posjecen, u udaljenosti dodajemo rezultat koji bi se dobio kada bismo iz trenutnog isli u taj grad
                    udaljenosti.append(vrati_udaljenost(prethodni_grad, i) + pronadi_najmanju_udaljenost(posjeceni_gradovi[:i] + "1" + posjeceni_gradovi[i + 1:], i))
            result = min(udaljenosti)  # rezultat je najmanja udaljenost

        rezultati_rekurzije[posjeceni_gradovi + str(prethodni_grad)] = result  # posto rezultat rekurzije s ovim parametrima nismo jos imali, spremimo ga za ubuduce
        return result  # vratimo rezultat


# unos broja gradova i matrice udaljenosti izmedu gradova
broj_gradova = int(input())
udaljenosti = []
for x in range(broj_gradova):
    udaljenosti.append(list(map(int, input().split(" "))))

# string kojim cemo pratiti posjecene gradove kroz rekurziju
posjeceni_gradovi = "0" * broj_gradova  # 0 znaci da nije posjecen
posjeceni_gradovi = "1" + posjeceni_gradovi[1:]  # prvi grad stavljamo na 1 (posjecen) jer iz njega krecemo

rezultati_rekurzije = dict()  # kako cemo mnogo puta rekurzivnu funkciju zvati s istim argumentima, spremimo rezultate u dictionary kako bismo ih lako dohvatili umjesto da mora rekurzija ispocetka racunati

najmanja_udaljenost = pronadi_najmanju_udaljenost(posjeceni_gradovi, 0)  # vrijednost najmanje udaljenosti koju vrati rekurzija, argumenti su string koji prati posjecene gradove i indeks prvog grada (0)

print(najmanja_udaljenost)  # ispis
