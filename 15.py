from pprint import pprint
from collections import *
from itertools import *
from heapq import *

from math import inf

fname = "test.txt"
fname = "in/15.txt"


with open(fname) as f:
    cave = [[int(i) for i in l.strip()] for l in f]

_cave = []
big_cave = []
for l in cave:
    ll = []
    for i in range(0, 5):
        ll.extend((x + i) % 9 or (x + i) for x in l)
    _cave.append(ll)

for i in range(0, 5):
    ll = []
    for l in _cave:
        ll.append([(x + i) % 9 or (x + i) for x in l])
    big_cave.extend(ll)

cave = big_cave
start = (0, 0)

distances = [[inf for _ in cave[0]] for _ in cave]
distances[0][0] = 0
visited = set()

q = [(0, start)]

while q:
    d, (x, y) = heappop(q)

    dx = x + 1
    ddx = x - 1
    dy = y + 1
    ddy = y - 1

    ngb = []

    for nx, ny in [(dx, y), (x, dy), (ddx, y), (x, ddy)]:
        if (nx, ny) in visited:
            continue
        if nx >= len(cave[0]) or nx < 0:
            continue
        if ny >= len(cave) or ny < 0:
            continue
        # print(nx, ny)

        nv = cave[ny][nx]
        ngb.append((nv, (nx, ny)))

    # ngb.sort(key=lambda x: [0])

    for w, v in ngb:
        dw = w + d
        if distances[v[1]][v[0]] > dw:
            distances[v[1]][v[0]] = dw
            heappush(q, (dw, v))

    visited.add((x, y))

# pprint(cave[-2][-10:])
# pprint(cave[-1][-10:])

# pprint(distances[-2][-10:])
# pprint(distances[-1][-10:])
# pprint(distances)
print(distances[-1][-1])
