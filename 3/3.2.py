import pandas as pd

f = open("i", "r")
lines = f.read().split("\n")
input = [[int(char) for char in line] for line in lines]


def asd(df, a, b):
    for col in df.columns:
        l = len(df)

        if l == 1:
            break

        if sum(df[col]) >= l / 2:
            df = df[df[col] == a]
        else:
            df = df[df[col] == b]

    r = [str(int(df[c])) for c in df.columns]

    bin_str = "".join(r)

    return int(bin_str, 2)


res1 = asd(pd.DataFrame(input), 1, 0)
res2 = asd(pd.DataFrame(input), 0, 1)


print(res1 * res2)
