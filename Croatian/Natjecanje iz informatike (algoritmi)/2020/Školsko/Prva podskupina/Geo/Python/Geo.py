n = int(input())
geohash = int(input())

bin_hash = f"{geohash:b}".zfill(2 * n)

x_celija = [x for x in range(1, pow(2, n) + 1)]
y_celija = x_celija.copy()

x_pass = 0
y_pass = 1
while len(x_celija) > 1:
	zbroj = 0
	for i in range(len(x_celija)):
		zbroj += x_celija[i]
	arith = zbroj / len(x_celija)

	if int(bin_hash[x_pass]) == 0:
		x_celija = [x for x in x_celija if x < arith]
	else:
		x_celija = [x for x in x_celija if x > arith]

	x_pass += 2

while len(y_celija) > 1:
	zbroj = 0
	for i in range(len(y_celija)):
		zbroj += y_celija[i]
	arith = zbroj / len(y_celija)

	if int(bin_hash[y_pass]) == 0:
		y_celija = [x for x in y_celija if x < arith]
	else:
		y_celija = [x for x in y_celija if x > arith]

	y_pass += 2

print(f"{x_celija[0] - 1} {y_celija[0] - 1}")
# presporo za veće brojeve (primjeri 9 i 10)
