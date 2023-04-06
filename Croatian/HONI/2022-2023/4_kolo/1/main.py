def main():
	goals_1 = int(input())
	goals_2 = int(input())

	if abs((goals_1 - goals_2)) < 7:
		print("NE")
	else:
		print("DA")


if __name__ == "__main__":
	main()
