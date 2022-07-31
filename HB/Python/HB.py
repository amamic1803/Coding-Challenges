ulaz = input()
izlaz = ""

en_u_hr = {
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
hr_u_en = {
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

if "Bb" in ulaz:
	radni_dict = en_u_hr
else:
	radni_dict = hr_u_en

while len(ulaz) > 0:
	try:
		izlaz += radni_dict[ulaz[0] + ulaz[1]]
		ulaz = ulaz[2:]
	except (IndexError, KeyError):
		izlaz += radni_dict[ulaz[0]]
		ulaz = ulaz[1:]

print(izlaz)
