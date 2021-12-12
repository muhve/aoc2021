f = open("i", "r")
lines = [int(i) for i in f.read().split(",")]
DAYS = 80
l = lines

for d in range(DAYS):
    for i in range(0, len(lines)):
        if lines[i] == 0:
            lines[i] = 6
            lines.append(8)
        else:
            lines[i] -= 1

print(len(lines))