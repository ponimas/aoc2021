from pprint import pprint
from collections import *
from itertools import *
from heapq import *

fname = "test.txt"
fname = "in/15.txt"


with open(fname) as f:
    cave = [[int(i) for i in l.strip()] for l in f]

BOLD = "\033[1m"
END = "\033[0m"


def pretty(path):
    pth = set(path)
    for y, l in enumerate(cave):
        p = ""
        for x, s in enumerate(l):
            if (x, y) in pth:
                p += BOLD + str(s) + END
            else:
                p += str(s)
        print(p)


start = (0, 0)

paths = [(0, (start,))]

end = (len(cave[0]) - 1, len(cave) - 1)


while True:
    weight, path = heappop(paths)
    x, y = path[-1]

    if (x, y) == end:
        pretty(path)
        print()
        print(weight)
        break

    dx, dy = x + 1, y + 1

    if dx <= end[0]:
        heappush(paths, (weight + cave[y][dx], (*path, (dx, y))))
    if dy <= end[1]:
        heappush(paths, (weight + cave[dy][x], (*path, (x, dy))))
