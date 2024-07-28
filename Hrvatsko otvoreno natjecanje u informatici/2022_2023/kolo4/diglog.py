def main():
	broj_pitanja = int(input())

	broj_bodova = 0
	for _ in range(broj_pitanja):
		odgovor = input()
		tocan_odgovor = input()

		if "x" in odgovor:
			if odgovor == tocan_odgovor:
				broj_bodova += 4
			else:
				broj_bodova -= 1

	print(broj_bodova)  # njegovi odgovori
	print(broj_pitanja * 4)  # sve točno
	print(broj_pitanja * -1)  # sve krivo


if __name__ == "__main__":
	main()
