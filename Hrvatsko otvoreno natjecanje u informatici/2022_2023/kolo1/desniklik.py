def main():
    broj_nfp, broj_redaka, _ = map(int, input().split())
    for _ in range(broj_nfp):
        prvi = None
        drugi = None
        for i in range(broj_redaka):
            if "#" in input():
                if prvi is None:
                    prvi = i
                drugi = i
        print(drugi - prvi)


if __name__ == '__main__':
    main()
