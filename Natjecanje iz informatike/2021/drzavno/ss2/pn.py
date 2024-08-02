def main():
	r1, s1 = map(int, input().split())
	r2, s2 = map(int, input().split())

	zbroj = 0

	# iz svakog retka izlučiti prvi član
	# tada redovi postanu 0 2 4 6 ...
	# takvih redova ima r2 - r1 + 1
	# a zbroj onih članova reda koji su u polju je s2 * (s2 - 1) - (s1 - 1) * (s1 - 2)

	zbroj += (r2 - r1 + 1) * (s2 * (s2 - 1) - (s1 - 1) * (s1 - 2))

	# treba pronaći 1. član svakog retka i dodati ga n puta za svaki red
	# gdje je n broj koliko je članova reda u polju (jer je iz njih izlučen 1. član)
	# n = s2 - s1 + 1

	n = s2 - s1 + 1

	# prvi član reda r1
	prvi_clan = (r1 * r1) // 2 - r1 + 2

	# razlika između prvog člana retka r1 i sljedećeg retka
	pomak = r1 if r1 % 2 == 1 else r1 - 1

	# zastavica koja označava paran ili neparan red
	zastavica = r1 % 2 == 0

	# za svaki red između r1 i r2
	for _ in range(r2 - r1 + 1):
		# dodati prvi član reda n puta
		zbroj += prvi_clan * n

		# izračunati prvi član sljedećeg retka
		prvi_clan += pomak

		# ako je red paran povećati pomak za 2
		if zastavica:
			pomak += 2

		# promijeniti zastavicu
		zastavica = not zastavica

	# ispisati zbroj
	print(zbroj)


if __name__ == "__main__":
	main()
