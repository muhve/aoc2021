f = open("i", "r")
asd = f.read().split("\n\n")
input_start = asd[0]
input_end = asd[1]

dots = [[int(n) for n in i.split(",")] for i in input_start.split("\n")]

input_end = [[n for n in i.split("=")] for i in input_end.split("\n")]
folds = [[i[0][-1], int(i[1])] for i in input_end]

max_x = max([dot[0] for dot in dots])
max_y = max([dot[1] for dot in dots])

paper = [[0] * (max_x + 1) for i in range(max_y + 1)]

for dot in dots:
    paper[dot[1]][dot[0]] = 1


def fold_y(paper, pos):
    half1 = [line for line in paper[:pos]]
    half2 = [line for line in paper[pos + 1 :]]

    new_max_y = len(half1) - 1

    for y in range(len(half2)):
        for x in range(len(half2[0])):
            if half2[y][x] == 1:
                half1[new_max_y - y][x] = 1

    return half1


def fold_x(paper, pos):
    half1 = [line[:pos] for line in paper]
    half2 = [line[pos + 1 :] for line in paper]

    new_max_x = len(half1[0]) - 1

    for y in range(len(half2)):
        for x in range(len(half2[0])):
            if half2[y][x] == 1:
                half1[y][new_max_x - x] = 1
    return half1


for fold in folds:
    axis = fold[0]
    pos = fold[1]

    if axis == "y":
        paper = fold_y(paper, pos)
    elif axis == "x":
        paper = fold_x(paper, pos)


for line in paper:
    print(["".join(["#" if x else "." for x in line])])