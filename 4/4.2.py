f = open("i", "r")
lines = f.read().split("\n\n")

l = lines.pop(0).split(",")

boards = []

for x in lines:
    b = x.split("\n")
    b = [r.split() for r in b]
    boards.append(b)


def loop(boards, l):
    for n in l:

        winning_boards = []
        for i in range(len(boards)):
            board = boards[i]

            for j in range(len(board)):
                row = board[j]
                boards[i][j] = [True if x == n else x for x in row]

                if all([x == True for x in boards[i][j]]):
                    winning_boards.append(i)

        for i in range(len(boards)):
            board = list(map(list, zip(*boards[i])))

            for j in range(len(board)):

                if all([x == True for x in board[j]]):
                    winning_boards.append(i)

        winning_boards = list(set(winning_boards))

        if len(boards) == 1 and len(winning_boards) == 1:
            return (boards[0], n)

        for i in sorted(winning_boards, reverse=True):
            del boards[i]


board, n = loop(boards, l)

sum = 0

for row in board:
    for i in row:
        if i != True:
            sum += int(i)

print(sum * int(n))
