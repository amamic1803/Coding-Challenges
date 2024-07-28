def main():
	br_osoba = int(input()) + 1
	br_foto = int(input())

	dobre_foto = 0

	for _ in range(br_foto):
		if int(input()) == br_osoba:
			dobre_foto += 1

	print(dobre_foto)


if __name__ == '__main__':
	main()
