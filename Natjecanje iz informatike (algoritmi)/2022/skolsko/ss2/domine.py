def main():
    redova, stupaca = map(int, input().split())

    matrica = []
    for x in range(redova):
        red = []
        for i in input():
            red.append(i)
        matrica.append(red)

    matrica = Matrix(redova, stupaca, matrica)
    print(matrica.dobrih_redova())


class Matrix:
    COLOR_SWITCH = {".": "#", "#": "."}  # bijela (".") -> crna, crna ("#") -> bijela

    def __init__(self, rows: int, cols: int, matrix: list[list[str]]):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix

    def dobrih_redova(self) -> int:
        return sum(1 for i in range(self.rows - 1) if self.dobar_red(self.matrix[i:i + 2]))

    def dobar_red(self, two_rows: list[list[str]]) -> bool:
        pozicija = None
        brk = False
        for i in range(2):
            for j in range(self.cols):
                if two_rows[i][j] != "x":
                    brk = True
                    pozicija = (i, j)
                    break
            if brk:
                break

        if pozicija is None:
            return True
        else:
            mog_polozaji = []
            boja_pozicije = two_rows[pozicija[0]][pozicija[1]]
            if pozicija[0] == 0 and pozicija[1] == 0:
                mog_polozaji.append((1, pozicija[1]))
                mog_polozaji.append((0, pozicija[1] + 1))
            elif pozicija[0] == 0 and pozicija[1] == self.cols - 1:
                mog_polozaji.append((1, pozicija[1]))
                mog_polozaji.append((0, pozicija[1] - 1))
            elif pozicija[0] == 0:
                mog_polozaji.append((1, pozicija[1]))
                mog_polozaji.append((0, pozicija[1] - 1))
                mog_polozaji.append((0, pozicija[1] + 1))
            elif pozicija[0] == 1 and pozicija[1] == 0:
                mog_polozaji.append((0, pozicija[1]))
                mog_polozaji.append((1, pozicija[1] + 1))
            elif pozicija[0] == 1 and pozicija[1] == self.cols - 1:
                mog_polozaji.append((0, pozicija[1]))
                mog_polozaji.append((1, pozicija[1] - 1))
            elif pozicija[0] == 1:
                mog_polozaji.append((0, pozicija[1]))
                mog_polozaji.append((1, pozicija[1] - 1))
                mog_polozaji.append((1, pozicija[1] + 1))

            izbrisano = 0
            for i in range(len(mog_polozaji)):
                if two_rows[mog_polozaji[i - izbrisano][0]][mog_polozaji[i - izbrisano][1]] == "x":
                    mog_polozaji.pop(i - izbrisano)
                    izbrisano += 1
                elif two_rows[mog_polozaji[i - izbrisano][0]][mog_polozaji[i - izbrisano][1]] != self.COLOR_SWITCH[boja_pozicije]:
                    mog_polozaji.pop(i - izbrisano)
                    izbrisano += 1
            postoji_kombinacija = False

            for i in mog_polozaji:
                two_rows[pozicija[0]][pozicija[1]] = "x"
                two_rows[i[0]][i[1]] = "x"

                recursive_result = self.dobar_red(two_rows)

                two_rows[pozicija[0]][pozicija[1]] = boja_pozicije
                two_rows[i[0]][i[1]] = self.COLOR_SWITCH[boja_pozicije]

                if recursive_result:
                    postoji_kombinacija = True
                    break

            if postoji_kombinacija:
                return True
            else:
                return False


if __name__ == "__main__":
    main()
