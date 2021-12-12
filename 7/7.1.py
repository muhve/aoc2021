f = open("i", "r")
lines = [int(i) for i in f.read().split(",")]

res = []

for n in range(max(lines)):
    res.append(sum([abs(i - n) for i in lines]))

print(min(res))