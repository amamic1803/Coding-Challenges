#!/usr/bin/python3

def main():
    # unos broja gradova i matrice udaljenosti izmedu gradova
    broj_gradova = int(input())
    udaljenosti = []
    for x in range(broj_gradova):
        udaljenosti.append(list(map(int, input().split(" "))))

    graph = Graph(broj_gradova, udaljenosti)
    print(graph.najmanja_udaljenost())


class Graph:
    def __init__(self, broj_gradova: int, udaljenosti: list[list[int]]):
        self.broj_gradova = broj_gradova
        self.udaljenosti = udaljenosti
        self.rezultati_rekurzije = None

    def get_edge(self, vertex1: int, vertex2: int) -> int:
        return self.udaljenosti[vertex1][vertex2]

    def najmanja_udaljenost(self):
        # string kojim cemo pratiti posjecene gradove kroz rekurziju
        # 0 znaci da grad nije posjecen
        # prvi grad stavljamo na 1 (posjecen) jer iz njega krecemo
        posjeceni_gradovi = "0" * self.broj_gradova
        posjeceni_gradovi = "1" + posjeceni_gradovi[1:]

        # kako cemo mnogo puta rekurzivnu funkciju zvati s istim argumentima,
        # spremimo rezultate u dictionary kako bismo ih lako dohvatili umjesto
        # da rekurzija mora ispocetka racunati
        self.rezultati_rekurzije = dict()

        # vrijednost najmanje udaljenosti koju vrati rekurzija,
        # argumenti su string koji prati posjecene gradove i indeks prvog grada (0)
        najmanja_udaljenost = self.najmanja_udaljenost_recursive(posjeceni_gradovi, 0)

        self.rezultati_rekurzije = None

        return najmanja_udaljenost

    def najmanja_udaljenost_recursive(self, posjeceni_gradovi, prethodni_grad):
        try:
            # ako vec imamo rezultat za funkciju pozvanu s ovim argumentima, vratimo tu vrijednost
            return self.rezultati_rekurzije[posjeceni_gradovi + str(prethodni_grad)]
        except KeyError:
            # ako nemamo moramo izracunati
            # ako je ostao jos jedan grad za posjetiti (Rim)
            # udaljenost od trenutnog grada do Rima spremimo u varijablu result
            if posjeceni_gradovi.count("0") == 1:
                result = self.get_edge(prethodni_grad, self.broj_gradova - 1)
            else:
                # ako ima vise neposjecenih gradova moramo provjeriti udaljenosti do svakog
                udaljenosti = []
                # krecemo od 1 nadalje jer je jedan sigurno posjecen (odande krecemo)
                # i stajemo prije zadnjeg jer je zadnji Rim (a njega rjesava druga grana if-a)
                for i in range(1, len(posjeceni_gradovi) - 1):
                    # ako trenutni grad nije posjecen, u udaljenosti dodajemo rezultat
                    # koji bi se dobio kada bismo iz trenutnog isli u taj grad
                    if posjeceni_gradovi[i] == "0":
                        udaljenosti.append(self.get_edge(prethodni_grad, i) + self.najmanja_udaljenost_recursive(
                            posjeceni_gradovi[:i] + "1" + posjeceni_gradovi[i + 1:], i)
                                           )
                result = min(udaljenosti)  # rezultat je najmanja udaljenost

            # posto rezultat rekurzije s ovim parametrima nismo jos imali, spremimo ga za kasnije
            self.rezultati_rekurzije[posjeceni_gradovi + str(prethodni_grad)] = result
            return result  # vratimo rezultat


if __name__ == "__main__":
    main()
