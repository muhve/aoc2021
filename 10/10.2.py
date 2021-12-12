f = open("i", "r")
lines = f.read().split("\n")

porints = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

scores = []

for i in range(len(lines)):
    line = lines[i]

    stack = []
    score = 0

    for char in line:

        if char in "([{<":
            stack.append(char)

        else:
            c = stack.pop()
            if c == pairs[char]:
                continue
            else:

                break
    else:
        while len(stack) > 0:
            c = stack.pop()

            score *= 5
            score += porints[c]

        scores.append(score)

print(sorted(scores)[int(len(scores) / 2)])