def main():
    input()
    blokovi = [x for x in input()]
    removed_value = blokovi.pop(int(input()) - 1)
    blokovi.append(removed_value)
    print("".join(blokovi))


if __name__ == "__main__":
    main()
