import copy

def main():
	r, s = map(int, input().split())
	board = []
	for _ in range(r):
		board.append(list(map(lambda x: x == "1", input().split())))

	max_jumps = 0
	checked_positions = copy.deepcopy(board)

	for i in range(r):
		for j in range(s):
			if checked_positions[i][j]:
				start_position = (i, j)
				reached_positions = flood_fill(start_position, board, r, s)
				max_jumps = max(max_jumps, len(reached_positions))
				for (r_i, r_j) in reached_positions:
					checked_positions[r_i][r_j] = False

	print(max_jumps)


def flood_fill(start_position: (int, int), board: [[bool]], r: int, s: int) -> set[(int, int)]:
	reached_positions = set()

	temp_positions = set()
	temp_positions.add(start_position)

	while len(temp_positions) != 0:
		current_position = temp_positions.pop()
		reached_positions.add(current_position)
		for neighbour in knight_jumps(current_position, r, s):
			if board[neighbour[0]][neighbour[1]] and neighbour not in reached_positions:
				temp_positions.add(neighbour)

	return reached_positions


def knight_jumps(start_position: (int, int), r: int, s: int):
	offsets = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
	for offset in offsets:
		new_position = (start_position[0] + offset[0], start_position[1] + offset[1])
		if 0 <= new_position[0] < r and 0 <= new_position[1] < s:
			yield new_position


if __name__ == "__main__":
	main()
