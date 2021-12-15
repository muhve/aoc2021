f = open("i", "r")
lines = [[int(n) for n in i] for i in f.read().split("\n")]

nodes = []
G = {}

cave = [[0] * (len(lines[0]) * 5) for i in range(len(lines) * 5)]

for y in range(len(lines)):
    for x in range(len(lines[0])):
        for i in range(5):
            val = ((lines[y][x] - 1 + i) % 9) + 1
            cave[y + i * len(lines)][x] = val

for n in range(5):
    for y in range(len(lines)):
        cur_y = y + n * len(lines)
        for x in range(len(lines[0])):
            for i in range(5):
                val = ((cave[cur_y][x] - 1 + i) % 9) + 1
                cave[cur_y][x + i * len(lines[0])] = val

for y in range(len(cave)):
    for x in range(len(cave[0])):
        G[(x, y)] = {}
        nodes.append((x, y))

        if x + 1 < len(cave[0]):
            G[(x, y)][(x + 1, y)] = cave[y][x + 1]

        if x - 1 >= 0:
            G[(x, y)][(x - 1, y)] = cave[y][x - 1]

        if y + 1 < len(cave):
            G[(x, y)][(x, y + 1)] = cave[y + 1][x]

        if y - 1 >= 0:
            G[(x, y)][(x, y - 1)] = cave[y - 1][x]

import heapq as hq

start = (0, 0)
visited = {}
weights = {}
queue = []
weights[start] = 0

hq.heappush(queue, (0, start))

while len(queue) > 0:
    distance_here, current_node = hq.heappop(queue)
    visited[current_node] = True

    for next_node, distance_next in G[current_node].items():
        if next_node not in visited.keys():
            distance = distance_here + distance_next

            if next_node not in weights.keys() or distance < weights[next_node]:
                weights[next_node] = distance
                hq.heappush(queue, (distance, next_node))


print(weights[(499, 499)])
