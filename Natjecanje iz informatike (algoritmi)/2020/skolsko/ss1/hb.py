EN_TO_HR = {
	"C": "C",
	"C#": "C#",
	"Db": "C#",
	"D": "D",
	"D#": "D#",
	"Eb": "D#",
	"E": "E",
	"F": "F",
	"F#": "F#",
	"Gb": "F#",
	"G": "G",
	"G#": "G#",
	"Ab": "G#",
	"A": "A",
	"A#": "A#",
	"Bb": "A#",
	"B": "H"
}
HR_TO_EN = {
	"C": "C",
	"C#": "C#",
	"Db": "C#",
	"D": "D",
	"D#": "D#",
	"Eb": "D#",
	"E": "E",
	"F": "F",
	"F#": "F#",
	"Gb": "F#",
	"G": "G",
	"G#": "G#",
	"Ab": "G#",
	"A": "A",
	"A#": "A#",
	"B": "A#",
	"H": "B"
}


def main():
	ulaz = input()

	if "Bb" in ulaz:
		radni_dict = EN_TO_HR
	else:
		radni_dict = HR_TO_EN

	while len(ulaz) > 0:
		try:
			print(radni_dict[ulaz[0] + ulaz[1]], end="")
			ulaz = ulaz[2:]
		except (IndexError, KeyError):
			print(radni_dict[ulaz[0]], end="")
			ulaz = ulaz[1:]

	print()


if __name__ == "__main__":
	main()
