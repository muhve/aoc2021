f = open("i", "r")
lines = f.read().split("\n")

input = []

for line in lines:
    a, b = line.split(" -> ")
    c = [int(x) for x in a.split(",")], [int(x) for x in b.split(",")]
    input.append(c)

res = [[0] * 1000 for i in range(1000)]

for line in input:
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]

    # horizontal

    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                res[i][x1] += 1
        else:
            for i in range(y2, y1 + 1):
                res[i][x1] += 1

    # vertical

    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                res[y1][i] += 1
        else:
            for i in range(x2, x1 + 1):
                res[y1][i] += 1

    # diagonal

    c = 0

    if x1 < x2:
        if y1 < y2:
            for i in range(x1, x2 + 1):
                res[y1 + c][i] += 1
                c += 1
        if y2 < y1:
            for i in range(x1, x2 + 1):
                res[y1 + c][i] += 1
                c -= 1

    elif x2 < x1:
        if y1 < y2:
            for i in range(x2, x1 + 1):
                res[y2 + c][i] += 1
                c -= 1
        if y2 < y1:
            for i in range(x2, x1 + 1):
                res[y2 + c][i] += 1
                c += 1

count = 0
for r in res:
    for x in r:
        if x > 1:
            count += 1

print(count)