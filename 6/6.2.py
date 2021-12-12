f = open("i", "r")
lines = [int(i) for i in f.read().split(",")]
DAYS = 256

phases = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(lines)):
    phases[lines[i]] += 1

for d in range(DAYS):
    new_phases = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(phases)):
        if i == 0:
            new_phases[6] = phases[0]
            new_phases[8] = phases[0]
        else:
            new_phases[i - 1] += phases[i]
    phases = new_phases.copy()

print(sum(phases))