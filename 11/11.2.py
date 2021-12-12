f = open("i", "r")
lines = [[int(x) for x in list(i)] for i in f.read().split("\n")]


def flash(x, y, arr):
    arr[y][x] = 0

    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if a == 0 and b == 0:
                continue

            elif (
                y + a >= 0
                and x + b >= 0
                and y + a < len(arr)
                and x + b < len(arr[0])
                and arr[y + a][x + b] > 0
            ):
                arr[y + a][x + b] += 1


def inc_all(arr):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            arr[y][x] += 1


def print_arr(lines):
    print()
    for line in lines:
        print("".join([str(i) for i in line]))
    print()


for n in range(1000):
    # print(f"step {n}")
    # print_arr(lines)
    inc_all(lines)

    done = False
    new_flashes = 0

    while not done:
        done = True
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] > 9:
                    done = False
                    flash(x, y, lines)
                    new_flashes += 1

    all_flash = all([all([True if n == 0 else False for n in line]) for line in lines])

    if all_flash:
        break

print(n + 1)
