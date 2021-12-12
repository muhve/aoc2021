f = open("i", "r")
lines = [[int(x) for x in list(i)] for i in f.read().split("\n")]


def check_adjacent(x, y):
    xy = lines[y][x]
    u = d = l = r = False

    if y > 0:
        u = lines[y - 1][x] > xy
    else:
        u = True

    if y < len(lines) - 1:
        d = lines[y + 1][x] > xy
    else:
        d = True

    if x > 0:
        l = lines[y][x - 1] > xy
    else:
        l = True

    if x < len(lines[0]) - 1:
        r = lines[y][x + 1] > xy
    else:
        r = True

    return u, d, l, r


res = 0

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        if all(check_adjacent(x, y)):
            res += lines[y][x] + 1

print(res)