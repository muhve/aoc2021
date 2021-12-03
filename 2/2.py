f = open("i", "r")
lines = f.read().split("\n")

pos = [0, 0]
aim = 0

input = []
for line in lines:
    input.append(line.split(" "))

for line in input:
    if line[0] == "forward":
        pos[0] += int(line[1])
        pos[1] += int(line[1]) * aim
    if line[0] == "up":
        aim -= int(line[1])
    if line[0] == "down":
        aim += int(line[1])

print(pos[0], pos[1])
print(pos[0] * pos[1])
