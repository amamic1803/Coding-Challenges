import itertools
import multiprocessing
# svi dodatni moduli korišteni za program

poliedar_len = sum(1 for num in itertools.combinations_with_replacement(range(0, 13), 18))  # dobiva duljinu generatora kombinacija za 18-strani poliedar (lista je prevelika pa se ne radi)
novcic_kom = list(itertools.combinations_with_replacement(range(0, 13), 2))  # radi listu s kombinacijama za novcic
novcic_len = len(novcic_kom)  # dobiva duljinu liste s kombinacijama za novcic

def checker(arg):
	# komentar 1. - Multiples of 3 or 5
	if arg == 1:
		rang_l = 0
		rang_h = int((1*(poliedar_len/4)) - 1)  # ovdje je rang_h jednog procesa manji od rang_l sljedećeg procesa jer se više ne koristi range formula za kombinacije poliedra
	elif arg == 2:
		rang_l = int(1*(poliedar_len/4))
		rang_h = int((2*(poliedar_len/4)) - 1)
	elif arg == 3:
		rang_l = int(2*(poliedar_len/4))
		rang_h = int((3*(poliedar_len/4)) - 1)
	else:
		rang_l = int(3*(poliedar_len/4))
		rang_h = int((4*(poliedar_len/4)) - 1)
	# sve između komentara 1. - Multiples of 3 or 5 i ovog komentara računa koji dio pojedini proces treba računati s obzirom na broj procesa koji je dobiven kao argument funkcije

	def checker_loop(range_low, range_high):  # funkcija u funkciji kako bi bilo lakše pratiti program
		counter = 0  # definira varijablu counter s vrijednosti 0, koristi se za podjelu posla po procesima jer se s generatorom ne može koristiti range kao s listom
		for poliedar in itertools.combinations_with_replacement(range(0, 13), 18):  # za svaku vrijednost u generatoru
			# komentar 2. - Even Fibonacci numbers
			if counter < range_low:
				counter += 1
				continue
			elif counter <= range_high:
				pass
			else:
				break
			# sve između komentara 2. - Even Fibonacci numbers i ovog komentara provjerava je li varijabla counter u određenom range-u koji je definiran za svaki proces posebno; ako nije, odmah se preskače kombinacija dobivena iz generatora

			for loop2 in range(0, novcic_len):
				novcic = novcic_kom[loop2]  # definira varijablu novcic za vrijednost loop2 u listi s kombinacijama za novcic
				if (max(poliedar) + max(novcic)) > 12 or (min(poliedar) + min(novcic)) < 2:  # provjerava da ne postoji mogućnost da se dobi broj veći od 12, ili broj manji od 2. - Even Fibonacci numbers, ako postoji automatski odbacuje kombinaciju; puno ubrzava rad programa
					continue
				# varijable test(broj) traže broj kombinacija od kojih se može složiti neki broj od novcica i poliedra; prvo se čiste(dodjeljuje im se vrijednost 0 prije provjeravanja)
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
				# ove dvije for formule ispod i if u njima dodjeljuju vrijednost varijablama test(broj) ovisno o broju kombinacija na koji se može složiti određeni broj od 2. - Even Fibonacci numbers do 12 od novcica i poliedra
				for x in poliedar:
					for y in novcic:
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
				# ova funkcija if provjerava je li broj kombinacija za varijable test(broj) isti kao i broj kombinacija za obične kocke i ako je ispisuje te kombinacije poliedra i novcica, ako nije ne događa se ništa i ide se na sljedeću kombinaciju poliedra i novcica
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
					print(poliedar, novcic)

			counter += 1  # dodaje jedan na varijablu counter ako je kombinacija uspješno prošla kroz program kako bi se moglo pratiti do kuda se u generatoru kombinacija za poliedar stiglo

	checker_loop(rang_l, rang_h)  # pokreće funkciju u funkciji imena checker_loop s dva argumenta, rang_l i rang_h


# dio programa ispod ovog komentara pokreće 4 zasebna procesa, kako bi program bio brži, tj. kako bi se moglo koristiti više jezgra procesora
if __name__ == "__main__":
	processes = []

	for draw in range(1, 5):
		p1 = multiprocessing.Process(target=checker, args=(draw,))  #pokreće funkciju checker s brojem procesa kao argumentom
		processes.append(p1)
		p1.start()

	for process in processes:
		process.join()
# program ispisuje 6 rješenja
