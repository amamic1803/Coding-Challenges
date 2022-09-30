r1, s1 = map(int, input().split())
r2, s2 = map(int, input().split())

jedinice_u_polju = (r2 - r1 + 1) * (s2 - s1 + 1)
vodoravno_zbrojeno = (r2 - r1 + 1) * (s2 * (s2 - 1) - (s1 - 1) * (s1 - 2))
vertikalno_zbrojeno = 0

trenutni_broj = (r1 * r1 - (r1 % 2)) // 2 - r1 + 1
vertikalno_zbrojeno += trenutni_broj
pomak = [r1 if r1 % 2 == 1 else r1 - 1, False if r1 % 2 == 0 else True]
for i in range(r1 + 1, r2 + 1):
	if pomak[1]:
		pomak[0] += 2
		vertikalno_zbrojeno += trenutni_broj + pomak[0]
		pomak[1] = False
	else:
		vertikalno_zbrojeno += trenutni_broj + pomak[0]
		pomak[1] = True
	trenutni_broj += pomak[0]

vertikalno_zbrojeno *= (s2 - s1 + 1)

print(jedinice_u_polju + vodoravno_zbrojeno + vertikalno_zbrojeno)
# ovaj način može biti sporiji od 1. - Multiples of 3 or 5 sekunde (ovisno o brzini procesora), isto rješenje u Rustu daje željenu brzinu (pogledajte folder Rust)
