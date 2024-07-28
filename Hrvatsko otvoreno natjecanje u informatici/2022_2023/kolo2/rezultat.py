def main():
	goals_needed_cro = int(input())
	goals_needed_sar = int(input())
	goals_in_game = int(input())
	curr_min = 0
	goals_cro = 0
	goals_sar = 0
	goals = []
	for _ in range(goals_in_game):
		goals.append([int(input()), int(input())])
	if (goals_cro - goals_sar > goals_needed_cro - goals_needed_sar) or (
			(goals_cro - goals_sar == goals_needed_cro - goals_needed_sar) and (goals_cro > goals_needed_cro)):
		found_winner = True
	else:
		found_winner = False
	for goal in goals:
		if (goals_cro - goals_sar > goals_needed_cro - goals_needed_sar) or ((goals_cro - goals_sar == goals_needed_cro - goals_needed_sar) and (goals_cro > goals_needed_cro)):
			found_winner = True
			break
		if goal[0] == 1:
			goals_cro += 1
		else:
			goals_sar += 1
		curr_min = goal[1]
	if (goals_cro - goals_sar > goals_needed_cro - goals_needed_sar) or (
			(goals_cro - goals_sar == goals_needed_cro - goals_needed_sar) and (goals_cro > goals_needed_cro)):
		found_winner = True
	if not found_winner:
		curr_min = 90
	print(f"{curr_min}\n{goals_cro}\n{goals_sar}")


if __name__ == '__main__':
	main()
