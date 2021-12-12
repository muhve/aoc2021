f = open("i", "r")
lines = [[int(x) for x in list(i)] for i in f.read().split("\n")]


def check_adjacent(x, y):
    xy = lines[y][x]
    u = d = l = r = False

    if xy == 9:
        return u, d, l, r

    if y > 0:
        u = lines[y - 1][x] >= xy
    else:
        u = True

    if y < len(lines) - 1:
        d = lines[y + 1][x] >= xy
    else:
        d = True

    if x > 0:
        l = lines[y][x - 1] >= xy
    else:
        l = True

    if x < len(lines[0]) - 1:
        r = lines[y][x + 1] >= xy
    else:
        r = True

    return u, d, l, r


def check_basin(x, y, basin):
    xy = lines[y][x]

    if xy == 9:
        return list(set(basin))

    if y > 0 and lines[y - 1][x] > xy:
        basin = check_basin(x, y - 1, basin + [(x, y)])

    if y < len(lines) - 1 and lines[y + 1][x] > xy:
        basin = check_basin(x, y + 1, basin + [(x, y)])

    if x > 0 and lines[y][x - 1] > xy:
        basin = check_basin(x - 1, y, basin + [(x, y)])

    if x < len(lines[0]) - 1 and lines[y][x + 1] > xy:
        basin = check_basin(x + 1, y, basin + [(x, y)])

    return list(set(basin + [(x, y)]))


low_points = []

for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):
        if all(check_adjacent(x, y)):
            low_points.append((x, y))

basins = []

for xy in low_points:
    basins.append(check_basin(xy[0], xy[1], []))

sizes = sorted([len(basin) for basin in basins])

res = sizes[-1] * sizes[-2] * sizes[-3]

print(res)