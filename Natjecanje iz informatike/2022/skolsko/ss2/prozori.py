#!/usr/bin/python3


def main():
    redaka, prozora_u_redu = map(int, input().split())

    vrste_prozora = {"A": ["....", "....", "....", "...."],
                     "B": ["####", "#..#", "#..#", "####"],
                     "C": ["....", ".##.", ".##.", "...."],
                     "D": ["####", "####", "####", "####"]}

    ispis_list = []

    for i in range(redaka):
        podaci_reda = input()

        for j in range(4):
            ispis = ""
            for x in podaci_reda:
                ispis += vrste_prozora[x][j]
            ispis_list.append(ispis)

    print("\n".join(ispis_list))


if __name__ == "__main__":
    main()
