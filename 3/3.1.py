f = open("i", "r")
lines = f.read().split("\n")


def gamma(lines):
    count = [0 for x in range(len(lines[0]))]

    for line in lines:
        for i in range(len(line)):
            count[i] += int(line[i])

    for i in range(len(count)):
        if count[i] > len(lines) / 2:
            count[i] = "1"
        else:
            count[i] = "0"

    res = "".join(count)
    print
    return int(res, 2)


def epsilon(lines):
    count = [0 for x in range(len(lines[0]))]

    for line in lines:
        for i in range(len(line)):
            count[i] += int(line[i])

    for i in range(len(count)):
        if count[i] < len(lines) / 2:
            count[i] = "1"
        else:
            count[i] = "0"

    res = "".join(count)
    return int(res, 2)


print(gamma(lines) * epsilon(lines))
