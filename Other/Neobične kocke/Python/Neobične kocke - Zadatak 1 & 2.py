import itertools
import multiprocessing
# svi dodatni moduli korišteni za program

kocka_kom = list(itertools.combinations_with_replacement(range(0, 13), 6))  # radi listu sa svim mogućim kombinacijama na jednoj kocki
kocka_len = len(kocka_kom)  # dobiva duljinu list iznad

def checker(arg):
	# komentar 1. - Multiples of 3 or 5
	if arg == 1:
		rang_l = 0
		rang_h = int(1*(kocka_len/4))
	elif arg == 2:
		rang_l = int(1*(kocka_len/4))  # rang_h nižeg procesa i rang_l sljedećeg procesa su isti jer formula range koju program koristi uzima broj manji od rang_h, ali isti kao i rang_l
		rang_h = int(2*(kocka_len/4))
	elif arg == 3:
		rang_l = int(2*(kocka_len/4))
		rang_h = int(3*(kocka_len/4))
	else:
		rang_l = int(3*(kocka_len/4))
		rang_h = int(4*(kocka_len/4))
	# sve između komentara 1. - Multiples of 3 or 5 i ovog komentara računa koji dio pojedini proces treba računati s obzirom na broj procesa koji je dobiven kao argument funkcije

	for loop1 in range(rang_l, rang_h):  # rang_l označuje dio liste s kombinacijama kocaka od kojeg treba krenuti određeni proces, a rang_h dio liste s kojim određeni proces završava
		kocka1 = kocka_kom[loop1]  # definira varijablu kocka1 za svaki loop1 (dio liste s kombinacijama kocaka)
		for loop2 in range(0, kocka_len):  # definira varijablu kocka2 za svaki loop2 u cijeloj listi s kombinacijama kocaka (nema razloga da se i kombinacije za kocku 2. - Even Fibonacci numbers dijele međuu procesima
			kocka2 = kocka_kom[loop2]
			if (max(kocka1) + max(kocka2)) > 12 or (min(kocka1) + min(kocka2)) < 2:  # provjerava da ne postoji mogućnost da se dobi broj veći od 12, ili broj manji od 2. - Even Fibonacci numbers, ako postoji automatski odbacuje kombinaciju; puno ubrzava rad programa
				continue
			# varijable test(broj) traže broj kombinacija od kojih se može složiti neki broj od dvije kocke; prvo se čiste(dodjeljuje im se vrijednost 0 prije provjeravanja)
			test2 = 0
			test3 = 0
			test4 = 0
			test5 = 0
			test6 = 0
			test7 = 0
			test8 = 0
			test9 = 0
			test10 = 0
			test11 = 0
			test12 = 0
			# ove dvije for formule ispod i if u njima dodjeljuju vrijednost varijablama test(broj) ovisno o broju kombinacija na koji se može složiti određeni broj od 2. - Even Fibonacci numbers do 12 od određene dvije kocke
			for x in kocka1:
				for y in kocka2:
					zbroj = x + y

					if zbroj == 2:
						test2 += 1
					elif zbroj == 3:
						test3 += 1
					elif zbroj == 4:
						test4 += 1
					elif zbroj == 5:
						test5 += 1
					elif zbroj == 6:
						test6 += 1
					elif zbroj == 7:
						test7 += 1
					elif zbroj == 8:
						test8 += 1
					elif zbroj == 9:
						test9 += 1
					elif zbroj == 10:
						test10 += 1
					elif zbroj == 11:
						test11 += 1
					elif zbroj == 12:
						test12 += 1
					else:
						pass

			# ova funkcija if provjerava je li broj kombinacija za varijable test(broj) isti kao i broj kombinacija za obične kocke i ako je ispisuje te kombinacije kocaka, ako nije ne događa se ništa i ide se na sljedeću kombinaciju kocaka
			if (test2 == 1 and
					test3 == 2 and
					test4 == 3 and
					test5 == 4 and
					test6 == 5 and
					test7 == 6 and
					test8 == 5 and
					test9 == 4 and
					test10 == 3 and
					test11 == 2 and
					test12 == 1):
				print(kocka1, kocka2)


# dio programa ispod ovog komentara pokreće 4 zasebna procesa, kako bi program bio brži, tj. kako bi se moglo koristiti više jezgra procesora
if __name__ == "__main__":
	processes = []

	for draw in range(1, 5):
		p1 = multiprocessing.Process(target=checker, args=(draw,))  #poziva funkciju checker
		processes.append(p1)
		p1.start()

	for process in processes:
		process.join()

# program ispisuje 9 rješenja, jedno već znamo (2. - Even Fibonacci numbers kocke od 1. - Multiples of 3 or 5 do 6), a ostalih osam su u parovima (zamijenjene prva i druga kocka) -> dakle postoji 4 rješenja
