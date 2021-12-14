f = open("i", "r")
lines = [i for i in f.read().split("\n")]
start = lines[0]

d = {}
c = {}

for line in lines[2:]:
    x = line.split(" -> ")
    d[x[0]] = [x[0][0] + x[1], x[1] + x[0][1]]
    c[x[0]] = 0

for i in range(len(start) - 1):
    pair = start[i : i + 2]
    c[pair] += 1

for n in range(10):
    new_c = c.copy()
    for key in c.keys():
        for inc_key in d[key]:

            new_c[inc_key] += c[key]

        new_c[key] -= c[key]
    c = new_c

counts = {}

for char in set("".join(c.keys())):
    counts[char] = {"start": 0, "end": 0}

for key in c:
    for i in [0, 1]:
        if key[i] in counts:
            if i == 0:
                counts[key[i]]["start"] += c[key]
            elif i == 1:
                counts[key[i]]["end"] += c[key]

res = {}

for key in counts.keys():
    res[key] = max(counts[key]["start"], counts[key]["end"])

print(max(res.values()) - min(res.values()))
