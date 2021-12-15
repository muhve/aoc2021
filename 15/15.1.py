f = open("i", "r")
lines = [[int(n) for n in i] for i in f.read().split("\n")]

nodes = []
G = {}

for y in range(len(lines)):
    for x in range(len(lines[0])):
        G[(x, y)] = {}
        nodes.append((x, y))

        if x + 1 < len(lines[0]):
            G[(x, y)][(x + 1, y)] = lines[y][x + 1]

        if x - 1 >= 0:
            G[(x, y)][(x - 1, y)] = lines[y][x - 1]

        if y + 1 < len(lines):
            G[(x, y)][(x, y + 1)] = lines[y + 1][x]

        if y - 1 >= 0:
            G[(x, y)][(x, y - 1)] = lines[y - 1][x]

unvisited = {node: None for node in nodes}
visited = {}
current = (0, 0)
current_distance = 0
unvisited[current] = current_distance

while True:
    for neighbour, distance in G[current].items():
        if neighbour not in unvisited:
            continue

        newDistance = current_distance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance

    visited[current] = current_distance
    del unvisited[current]

    if not unvisited:
        break

    candidates = [node for node in unvisited.items() if node[1]]
    current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

print(visited[(99, 99)])