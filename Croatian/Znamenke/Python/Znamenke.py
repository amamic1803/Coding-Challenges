N = int(input())
K = int(input())

veci_broj = [int(x) for x in str(N)]
manji_broj = [int(x) for x in str(N)]
razlika = sum(manji_broj) - K

if razlika == 0:  # ako upisani broj već ima zbroj znamenki K
	print(N)
else:
	if razlika > 0:  # treba smanjiti zbroj znamenaka u broju N
		# prvi veći - od kraja broja, na svakom mjestu smanjujemo znamenku koliko možemo, ali kada prvi put dođemo na neko mjesto, mjestu ispred dodamo jedan, a tom mjestu smanjimo 1, ponavljamo dok ne dođemo do uvjeta da je zbroj znamenki = K
		razlika_veci = razlika
		indeks = -1
		indeks_promijenjen = True
		while razlika_veci != 0:
			if veci_broj[indeks] == 0:
				indeks -= 1
				indeks_promijenjen = True
			elif indeks_promijenjen:
				try:
					veci_broj[indeks - 1] += 1
				except IndexError:
					veci_broj.insert(indeks - 1, 1)
				veci_broj[indeks] -= 1
				indeks_promijenjen = False
			else:
				if razlika_veci < veci_broj[indeks]:
					veci_broj.append(veci_broj[indeks] - razlika_veci)  # ako neko mjesto ne možemo više smanjiti do kraja (do 0), onda tu smanjenu znamenku mičemo i stavljamo na kraj broja
					veci_broj.pop(indeks - 1)
					razlika_veci = 0
				else:
					veci_broj[indeks] = 0
					razlika_veci = sum(veci_broj) - K
					indeks -= 1
					indeks_promijenjen = True
		while True:  # ako je na nekom mjestu ostala desetka (zbog uvjeta da moramo povećavati znamenku ispred kada prvi put dođemo na neko mjesto), tu desetku smanjimo za 1, a znamenku ispred povećamo za 1, desetku smanjenu za 1 mičemo i stavljamo na kraj broja, ponavljamo da se ne bi opet pojavila desetka (jer smo povećavali znamenku na mjestu ispred)
			try:
				indeks_desetke = veci_broj.index(10) - len(veci_broj)
				veci_broj.append(9)
				veci_broj.pop(indeks_desetke - 1)
				try:
					veci_broj[indeks_desetke - 1] += 1
				except IndexError:
					veci_broj.insert(indeks_desetke - 1, 1)
			except ValueError:
				break

		# prvi manji - od kraja broja, smanjujemo znamenku koliko možemo (do 0), onda idemo na znamenku ispred pa opet smanjujemo ... dok ne dođemo do uvjeta da je zbroj znamenki = K
		razlika_manji = razlika
		indeks = -1
		while razlika_manji != 0:
			oduzeti = min(razlika_manji, manji_broj[indeks])
			manji_broj[indeks] -= oduzeti
			indeks -= 1
			razlika_manji = sum(manji_broj) - K

	else:  # treba povećati zbroj znamenaka u broju N
		# prvi veći - od kraja broja, povećavamo znamenku koliko možemo (do 9), onda idemo na znamenku ispred pa opet povećavamo... dok ne dođemo do uvjeta da je zbroj znamenku = K
		razlika_veci = abs(razlika)
		indeks = -1
		while razlika_veci != 0:
			dodati = min(razlika_veci, 9 - veci_broj[indeks])
			veci_broj[indeks] += dodati
			indeks -= 1
			razlika_veci = K - sum(veci_broj)
			if len(veci_broj) == abs(indeks + 1) and razlika_veci != 0:
				veci_broj.insert(0, 0)

		# prvi manji - od kraja broja, na svakom mjestu povećavamo znamenku koliko možemo, ali kada prvi put dođemo na neko mjesto, mjestu ispred smanjimo jedan, a tom mjestu dodamo 1, ponavljamo dok ne dođemo do uvjeta da je zbroj znamenki = K
		razlika_manji = abs(razlika)
		indeks = -1
		indeks_promijenjen = True
		while razlika_manji != 0:
			if manji_broj[indeks] == 9:
				indeks -= 1
				indeks_promijenjen = True
			elif indeks_promijenjen:
				try:
					manji_broj[indeks - 1] -= 1
				except IndexError:
					manji_broj.insert(indeks - 1, -1)
				manji_broj[indeks] += 1
				indeks_promijenjen = False
			else:
				if razlika_manji < 9 - manji_broj[indeks]:
					manji_broj.append(manji_broj[indeks] + razlika_manji)  # ako neko mjesto ne možemo više povećati do kraja (do 9), onda tu povećanu znamenku mičemo i stavljamo na kraj broja
					manji_broj.pop(indeks - 1)
					razlika_manji = 0
				else:
					manji_broj[indeks] = 9
					razlika_manji = abs(sum(manji_broj) - K)
					indeks -= 1
					indeks_promijenjen = True
		while True:  # ako je na nekom mjestu ostao -1 (zbog uvjeta da moramo smanjiti znamenku ispred kada prvi put dođemo na neko mjesto), taj -1 povećamo za 1, a znamenku ispred smanjimo za 1, -1 povećan za 1 mičemo i stavljamo na kraj broja, ponavljamo da se ne bi opet pojavio -1 (jer smo smanjivali znamenku na mjestu ispred), ali prekidamo ako je -1 na prvom mjestu u broju (jer će se tada uvijek pojavljivati -1 na početku)
			try:
				indeks_minusa = manji_broj.index(-1) - len(manji_broj)
				if abs(indeks_minusa) == len(manji_broj):
					break
				manji_broj.append(0)
				manji_broj.pop(indeks_minusa - 1)
				try:
					manji_broj[indeks_minusa - 1] -= 1
				except IndexError:
					manji_broj.insert(indeks_minusa - 1, -1)
			except ValueError:
				break

	# pretvori u brojeve, pronađi koji je bliži i ispiši
	veci_broj = int("".join(map(str, veci_broj)))
	manji_broj = int("".join(map(str, manji_broj)))

	if manji_broj <= 0:
		print(veci_broj)
	elif abs(veci_broj - N) < abs(manji_broj - N):
		print(veci_broj)
	else:
		print(manji_broj)
