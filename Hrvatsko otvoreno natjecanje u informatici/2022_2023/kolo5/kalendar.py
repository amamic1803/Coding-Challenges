def main():
    print("+" + "-" * 21 + "+")

    broj_dana, pocetni_dan = map(int, input().split(" "))

    dani = ""
    pozicija = 1
    while pozicija < pocetni_dan:
        dani += "..."
        pozicija += 1

    for dan in range(1, broj_dana + 1):
        dan = str(dan)
        while len(dan) < 3:
            dan = "." + dan
        dani += dan
        pozicija += 1

    while pozicija % 7 != 1:
        dani += "..."
        pozicija += 1

    for i in range(0, len(dani), 21):
        print("|" + dani[i:i + 21] + "|")

    print("+" + "-" * 21 + "+")


if __name__ == '__main__':
    main()
