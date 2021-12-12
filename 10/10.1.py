f = open("i", "r")
lines = f.read().split("\n")

chars = "([{<)]}>"

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

error = []

for line in lines:
    stack = []

    for char in line:

        if char in "([{<":
            stack.append(char)

        else:
            c = stack.pop()
            if c == pairs[char]:
                continue
            else:
                error.append(scores[char])
                break


print(sum(error))