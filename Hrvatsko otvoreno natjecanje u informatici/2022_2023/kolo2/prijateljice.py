def main():
    br_rijeci_leona, br_rijeci_zoe = map(int, input().split(" "))
    rijeci_leona = [input() for _ in range(br_rijeci_leona)]
    rijeci_zoe = [input() for _ in range(br_rijeci_zoe)]

    rijeci_leona.sort(reverse=True)
    rijeci_zoe.sort(reverse=True)

    if len(rijeci_leona) == 0:
        print("Zoe")
        return

    # False == Leona, True == Zoe
    turn = True
    current_word = rijeci_leona.pop()

    try:
        while True:
            if turn:
                word = rijeci_zoe.pop()
                while word < current_word:
                    word = rijeci_zoe.pop()
                if ord(word[0]) - ord(current_word[0]) > 1:
                    break
                current_word = word
            else:
                word = rijeci_leona.pop()
                while word < current_word:
                    word = rijeci_leona.pop()
                if ord(word[0]) - ord(current_word[0]) > 1:
                    break
                current_word = word
            turn = not turn
    except IndexError:
        pass

    if turn:
        print("Leona")
    else:
        print("Zoe")


if __name__ == '__main__':
    main()
