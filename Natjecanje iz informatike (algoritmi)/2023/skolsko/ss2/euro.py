#!/usr/bin/python3

def main():
    # input
    # unos broja proizvoda
    broj_proizvoda = int(input())

    # unos proizvoda
    proizvodi = dict()
    sve_moguce_drzave = []  # odmah cemo izdvojiti koje su sve drzave moguce
    for i in range(broj_proizvoda):
        proizvod, drzava, cijena = input().split("-")
        cijena = float(cijena.replace(",", "."))

        try:
            proizvodi[proizvod]
        except KeyError:
            proizvodi[proizvod] = dict()

        proizvodi[proizvod][drzava] = cijena
        sve_moguce_drzave.append(drzava)
    sve_moguce_drzave = set(sve_moguce_drzave)  # pretvaramo u set i natrag kako bismo maknuli duplikate
    sve_moguce_drzave = list(sve_moguce_drzave)
    # sortiramo drzave jer ce kasnije biti potrebne sortirane kako bi bile ispisane abecednim redom (uvjet 1.)
    sve_moguce_drzave.sort()

    # za pojedini proizvod pronaci najmanju cijenu i u kojoj je drzavi
    for proizvod in proizvodi.keys():
        najmanja_cijena = 11_000
        drzava_min = ""
        for drzava in proizvodi[proizvod].keys():
            if proizvodi[proizvod][drzava] < najmanja_cijena:
                najmanja_cijena = proizvodi[proizvod][drzava]
                drzava_min = drzava
        proizvodi[proizvod] = [drzava_min, najmanja_cijena]

    # idemo po abecednom redu rjesavati drzavu po drzavu i ispisivati ako se ima sto ispisati
    for drzava in sve_moguce_drzave:

        # izdvojiti sve proizvode koje treba ispisati za tu drzavu i njihove cijene
        proizvodi_u_drzavi = []
        for proizvod in proizvodi.keys():
            if proizvodi[proizvod][0] == drzava:
                proizvodi_u_drzavi.append([proizvodi[proizvod][1], proizvod])  # [cijena, ime_proizvoda]

        # ponavljamo ovu petlju dok ne rijesimo sve proizvode u drzavi
        while len(proizvodi_u_drzavi) != 0:
            najmanja_cijena = min([x[0] for x in proizvodi_u_drzavi])  # pronadi koja je najmanja cijena u drzavi

            oni_s_najmanjom_cijenom = []  # pronadi proizvode u drzavi koji imaju tu najmanju cijenu
            izbrisano = 0
            for x in range(len(proizvodi_u_drzavi)):
                if proizvodi_u_drzavi[x - izbrisano][0] == najmanja_cijena:
                    oni_s_najmanjom_cijenom.append(proizvodi_u_drzavi[x - izbrisano][1])
                    proizvodi_u_drzavi.pop(x - izbrisano)
                    izbrisano += 1
            # pretvori u set i nazad da se izbrisu duplikati
            # (do kojih bi doslo kada bi isti upis bio ponovljen vise od jednom,
            # primjerice dva proizvoda bi imala isto ime, zemlju, cijenu)
            oni_s_najmanjom_cijenom = set(oni_s_najmanjom_cijenom)
            oni_s_najmanjom_cijenom = list(oni_s_najmanjom_cijenom)
            # sortiramo abecedno te proizvode u drzavi koji imaju najmanju cijenu jer ih tim redoslijedom treba ispisati
            oni_s_najmanjom_cijenom.sort()

            for pr in oni_s_najmanjom_cijenom:
                # ispis (output)
                print(f"{pr}-{drzava}-{f'{round(najmanja_cijena, 2):.2f}'.replace('.', ',')}")


if __name__ == "__main__":
    main()
