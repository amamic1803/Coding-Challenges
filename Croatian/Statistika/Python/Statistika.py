
class Datoteka:
	def __init__(self, razina, vrsta, velicina):
		self.razina = razina
		self.vrsta = vrsta
		self.velicina = velicina


broj_datoteka = int(input())
lista_datoteka = []
for x in range(1, broj_datoteka + 1):
	upis = input()
	upis_2 = upis.split(" ")
	upis_velicina = int(upis_2[-1])
	upis_3 = upis_2[0].split("/")
	upis_razina = len(upis_3) - 2
	upis_4 = upis_3[-1].split(".")
	upis_vrsta = "." + upis_4[-1]

	exec(f"datoteka_{x} = Datoteka(upis_razina, upis_vrsta, upis_velicina)")
	exec(f"lista_datoteka.append(datoteka_{x})")

broj_razina = 0
for x in range(len(lista_datoteka)):
	if lista_datoteka[x].razina > broj_razina:
		broj_razina = lista_datoteka[x].razina

for x in range(0, broj_razina + 1):

	ispis = [x]

	lista_datoteka_razine = []
	lista_vrsta_razine = []
	lista_velicina_razine = []
	broj_vrste = []

	for y in range(len(lista_datoteka)):
		if lista_datoteka[y].razina == x:
			lista_datoteka_razine.append(lista_datoteka[y])

	for y in range(len(lista_datoteka_razine)):
		if lista_datoteka_razine[y].vrsta not in lista_vrsta_razine:
			lista_vrsta_razine.append(lista_datoteka_razine[y].vrsta)

	for y in range(len(lista_vrsta_razine)):
		zbroj = 0
		for a in range(len(lista_datoteka_razine)):
			if lista_datoteka_razine[a].vrsta == lista_vrsta_razine[y]:
				zbroj += lista_datoteka_razine[a].velicina
		lista_velicina_razine.append(zbroj)

	for y in range(len(lista_vrsta_razine)):
		broj_vrste.append(0)

	for a in range(len(lista_vrsta_razine)):
		for b in range(len(lista_datoteka_razine)):
			if lista_datoteka_razine[b].vrsta == lista_vrsta_razine[a]:
				broj_vrste[a] += 1

	while len(lista_datoteka_razine) > 0:

		najveci_broj_datoteke = max(broj_vrste)
		broj_ponavljanja_najveceg_broja = 0
		for y in range(len(broj_vrste)):
			if broj_vrste[y] == najveci_broj_datoteke:
				broj_ponavljanja_najveceg_broja += 1

		if broj_ponavljanja_najveceg_broja == 1:
			idx = broj_vrste.index(max(broj_vrste))
			ispis.append(f"{lista_vrsta_razine[idx]} {lista_velicina_razine[idx]}")
			obrisano = 0
			for a in range(len(lista_datoteka_razine)):
				if lista_datoteka_razine[a - obrisano].vrsta == lista_vrsta_razine[idx]:
					del lista_datoteka_razine[a - obrisano]
					obrisano += 1
			del lista_vrsta_razine[idx]
			del lista_velicina_razine[idx]
			del broj_vrste[idx]
		else:
			najveca_velicina_datoteke = max(lista_velicina_razine)
			broj_ponavljanja_najvece_velicine = 0
			for a in range(len(lista_velicina_razine)):
				if lista_velicina_razine[a] == najveca_velicina_datoteke:
					broj_ponavljanja_najvece_velicine += 1

			if broj_ponavljanja_najvece_velicine == 1:
				idx = lista_velicina_razine.index(max(lista_velicina_razine))
				ispis.append(f"{lista_vrsta_razine[idx]} {lista_velicina_razine[idx]}")
				obrisano = 0
				for a in range(len(lista_datoteka_razine)):
					if lista_datoteka_razine[a - obrisano].vrsta == lista_vrsta_razine[idx]:
						del lista_datoteka_razine[a - obrisano]
						obrisano += 1
				del lista_vrsta_razine[idx]
				del lista_velicina_razine[idx]
				del broj_vrste[idx]
			else:
				lista_vrsta_razine_kopija = lista_vrsta_razine.copy()
				lista_vrsta_razine_kopija.sort()
				idx = lista_vrsta_razine.index(lista_vrsta_razine_kopija[0])
				ispis.append(f"{lista_vrsta_razine[idx]} {lista_velicina_razine[idx]}")
				obrisano = 0
				for a in range(len(lista_datoteka_razine)):
					if lista_datoteka_razine[a - obrisano].vrsta == lista_vrsta_razine[idx]:
						del lista_datoteka_razine[a - obrisano]
						obrisano += 1
				del lista_vrsta_razine[idx]
				del lista_velicina_razine[idx]
				del broj_vrste[idx]

	if len(ispis) != 1:
		for y in range(len(ispis)):
			print(ispis[y])
