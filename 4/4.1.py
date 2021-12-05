import pandas as pd

f = open("i", "r")
lines = f.read().split("\n\n")

l = lines.pop(0).split(",")

boards = []

print(l)

for x in lines:
    b = x.split("\n")
    b = [r.split() for r in b]
    boards.append(b)

# print(boards)


def loop(boards, l):
    for n in l:
        for i in range(len(boards)):
            board = boards[i]

            for j in range(len(board)):
                row = board[j]
                boards[i][j] = [True if x == n else x for x in row]
                if all([x == True for x in boards[i][j]]):
                    return (boards[i], n)

        for i in range(len(boards)):
            board = list(map(list, zip(*boards[i])))

            for j in range(len(board)):

                if all([x == True for x in board[j]]):
                    return (boards[i], n)


board, n = loop(boards, l)

sum = 0

for row in board:
    print(row)
    for i in row:
        if i != True:
            sum += int(i)

print(n)
print(sum)
print(sum * int(n))
# NOT 11067

"""
for n in l:
    boards = [
        [[True if x == n else x for x in row] for row in board] for board in boards
    ]
    print(boards)

"""