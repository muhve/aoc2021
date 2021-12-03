import pandas as pd

f = open("1.input", "r")
lines = f.read().split("\n")


counter = 0

for i in range(1, len(lines)):
    if int(lines[i]) > int(lines[i - 1]):
        counter += 1

print(counter)

df = pd.DataFrame(lines)

df["a"] = df[0].rolling(3).sum()
df = df.dropna()
counter = 0
for i in range(1, len(df["a"])):
    if int(df["a"].iloc[i]) > int(df["a"].iloc[i - 1]):
        counter += 1

print(counter)