#!/usr/bin/python3

r, s = map(int, input().split(" "))

lista_mjesta = []

for x in range(r):
    exec(f"red_{x + 1} = []")
    temp_inp = input()

    for y in range(len(temp_inp)):
        exec(f"red_{x + 1}.append(temp_inp[y])")

    exec(f"lista_mjesta.append(red_{x + 1})")

nadena_mjesta = 0

for x in range(len(lista_mjesta)):
    if x == 0 or x == len(lista_mjesta):
        continue
    else:
        for y in range(len(lista_mjesta[x])):
            if y == 0 or y == (len(lista_mjesta[x]) - 1):
                continue
            elif lista_mjesta[x][y] == ".":
                continue
            elif lista_mjesta[x][y - 1] == "#" and lista_mjesta[x][y + 1] == "#":
                continue
            elif lista_mjesta[x][y - 1] == "#" or lista_mjesta[x][y + 1] == "#":
                if lista_mjesta[x][y - 1] == "#" and (y - 1) != 0:
                    if lista_mjesta[x][y - 2] == "." and lista_mjesta[x][y + 1] == "." and lista_mjesta[x - 1][y - 2] == "." and lista_mjesta[x - 1][y - 1] == "." and lista_mjesta[x - 1][y] == "." and lista_mjesta[x - 1][y + 1] == "." and lista_mjesta[x + 1][y - 2] == "." and lista_mjesta[x + 1][y - 1] == "." and lista_mjesta[x + 1][y] == "." and lista_mjesta[x + 1][y + 1] == ".":
                        nadena_mjesta += 1
                if lista_mjesta[x][y + 1] == "#" and (y + 1) != (len(lista_mjesta[x]) - 1):
                    if lista_mjesta[x][y - 1] == "." and lista_mjesta[x][y + 2] == "." and lista_mjesta[x - 1][y - 1] == "." and lista_mjesta[x - 1][y] == "." and lista_mjesta[x - 1][y + 1] == "." and lista_mjesta[x - 1][y + 2] == "." and lista_mjesta[x + 1][y - 1] == "." and lista_mjesta[x + 1][y] == "." and lista_mjesta[x + 1][y + 1] == "." and lista_mjesta[x + 1][y + 2] == ".":
                        nadena_mjesta += 1

print(nadena_mjesta // 2)
