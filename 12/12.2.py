f = open("i", "r")
lines = [i.split("-") for i in f.read().split("\n")]

G = {}

for line in lines:
    if not line[0] in G.keys():
        G[line[0]] = [line[1]]
    else:
        G[line[0]].append(line[1])
    if not line[1] in G.keys():
        G[line[1]] = [line[0]]
    else:
        G[line[1]].append(line[0])


def dfs(G, u, target, visited, path, fullPath, extra):
    visited.append(u)
    path.append(u)

    if u == target:
        fullPath.append(list(path))

    for i in G[u]:
        if i not in visited or i.isupper():
            dfs(G, i, target, visited, path, fullPath, extra)
        elif extra and i != "end" and i != "start":
            dfs(G, i, target, visited, path, fullPath, False)

    path.pop()
    visited.pop()

    if not path:
        return fullPath


res = dfs(G, "start", "end", [], [], [], True)

for path in res:
    print(",".join(path))

print(len(res))
