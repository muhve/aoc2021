import collections

f = open("t", "r")
lines = [i for i in f.read().split("\n")]
start = lines[0]
d = {}
for line in lines[2:]:
    x = line.split(" -> ")
    d[x[0]] = x[1]


def most_and_least_common(string):
    return (
        collections.Counter(string).most_common(10)[0],
        collections.Counter(string).most_common(27)[-1],
    )


def step(start):
    new = ""

    for i in range(len(start) - 1):
        pair = start[i : i + 2]
        if pair in d.keys():
            new += pair[0] + d[pair]

    new += start[-1]

    return new


for n in range(10):
    start = step(start)

f = most_and_least_common(start)

print(f[0][1] - f[1][1])
