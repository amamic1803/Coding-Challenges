def main():
	price = int(input())
	for i in range(1, 4):
		temp_value = price % (10 ** i)
		print(temp_value)
		price -= temp_value


if __name__ == '__main__':
	main()
