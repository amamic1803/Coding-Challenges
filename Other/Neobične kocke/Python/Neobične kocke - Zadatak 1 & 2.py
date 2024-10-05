import itertools


WANTED_PROBABILITIES = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

def check_cubes(cubes):
	cube1, cube2 = cubes
	probabilities = [0 for _ in range(11)]

	break_flag = False
	for n1 in cube1:
		for n2 in cube2:
			value = n1 + n2 - 2
			if value < 0 or value > 10:
				break_flag = True
				break
			else:
				probabilities[value] += 1
		if break_flag:
			break

	if not break_flag and probabilities == WANTED_PROBABILITIES:
		return cube1, cube2
	else:
		return None

def solve():
	return filter(
		lambda x: x is not None,
		map(
			check_cubes,
			itertools.combinations_with_replacement(
				itertools.combinations_with_replacement(range(0, 13), 6),
				2
			),
		)
	)


if __name__ == "__main__":
	for cube1, cube2 in solve():
		print(" ".join(map(str, cube1)) + " --- " + " ".join(map(str, cube2)))
