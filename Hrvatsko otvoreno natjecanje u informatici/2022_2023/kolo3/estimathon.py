def main():
	br_stolova, br_boja = map(int, input().split(" "))
	boje_brojevi = list(map(int, input().split(" ")))

	if br_boja > br_stolova or min(boje_brojevi) < 4:
		rezultat = False
	else:
		cetvorki = 0
		for x in boje_brojevi:
			cetvorki += x // 4

		if cetvorki < br_stolova:
			rezultat = False
		else:
			rezultat = True

	if rezultat:
		print("DA")
	else:
		print("NE")


if __name__ == '__main__':
	main()
