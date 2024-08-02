def main():
	n = int(input())
	geohash = int(input())
	x, y = anti_geohash(n, geohash)
	print(f"{x} {y}")

def anti_geohash(grid_size: int, geohash: int) -> (int, int):
	# treba razdvojiti bitove geohasha na x i y
	# svaki drugi bit je x (počevši od najznačajnijeg), svaki drugi je y (počevši od drugog najznačajnijeg)

	rev_x, rev_y = 0, 0

	temp_hash = geohash
	for _ in range(grid_size):
		rev_y <<= 1
		rev_y |= temp_hash & 1
		temp_hash >>= 2

	temp_hash = geohash >> 1
	for _ in range(grid_size):
		rev_x <<= 1
		rev_x |= temp_hash & 1
		temp_hash >>= 2

	x, y = 0, 0
	for _ in range(grid_size):
		x <<= 1
		x |= rev_x & 1
		rev_x >>= 1
		y <<= 1
		y |= rev_y & 1
		rev_y >>= 1

	return x, y

def reverse_binary(n: int) -> int:
	new_n = 0
	while n != 0:
		new_n <<= 1
		new_n |= n & 1
		n >>= 1
	return new_n


if __name__ == '__main__':
	main()
