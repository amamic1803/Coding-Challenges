def main():
    broj_treninga = int(input())
    pretrcano_metara = sum(int(input()) for _ in range(broj_treninga))
    print(pretrcano_metara)
    if pretrcano_metara < 42_195:
        print("NE")
    else:
        print("DA")


if __name__ == '__main__':
    main()
