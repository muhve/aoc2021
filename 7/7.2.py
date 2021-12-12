f = open("i", "r")
lines = [int(i) for i in f.read().split(",")]

res = []

for n in range(max(lines)):
    fuels = []

    for i in lines:
        steps = abs(i - n)
        fuel = sum(range(steps + 1))
        fuels.append(fuel)

    res.append(sum(fuels))

print(min(res))