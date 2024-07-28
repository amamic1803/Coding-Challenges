def main():
	br_stanica = int(input())
	stanice = []
	for _ in range(br_stanica - 1):
		new_stanica = list(input().split(" "))
		new_stanica.extend(list(map(int, new_stanica[1:])))
		new_stanica.pop(1)
		if new_stanica[0] == "Josip":
			new_stanica.pop(1)
		stanice.append(new_stanica)
	stanice_times = [(1, 0)]
	for stanica in range(len(stanice)):
		if stanice[stanica][0] == "Patrik":
			stanice_times.append((stanica + 2, stanice[stanica][1]))
		else:
			stanice_times.append((stanica + 2, stanice_times[stanice[stanica][1] - 1][1]+ stanice[stanica][2]))

	minimal_time = stanice_times[-1][1]
	minimal_stanice = (1, stanice_times[-1][0])
	for i in range(1, len(stanice_times)):
		if stanice_times[i][1] - stanice_times[i - 1][1] < minimal_time:
			minimal_time = stanice_times[i][1] - stanice_times[i - 1][1]
			minimal_stanice = (stanice_times[i - 1][0], stanice_times[i][0])
	print(f"{minimal_time} {minimal_stanice[0]} {minimal_stanice[1]}")


if __name__ == '__main__':
	main()
