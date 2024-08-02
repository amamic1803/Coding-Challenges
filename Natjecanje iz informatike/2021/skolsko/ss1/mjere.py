def main():
	r, s = map(int, input().split(" "))

	dvorana = []
	for x in range(r):
		red = [x for x in input()]
		dvorana.append(red)

	nadena_mjesta = 0
	for x in range(1, r - 1):
		for y in range(1, s - 2):
			if dvorana[x][y - 1:y + 3] == [".", "#", "#", "."] and dvorana[x - 1][y - 1:y + 3] == [".", ".", ".", "."] and dvorana[x + 1][y - 1:y + 3] == [".", ".", ".", "."]:
				nadena_mjesta += 1

	print(nadena_mjesta)


if __name__ == "__main__":
	main()
