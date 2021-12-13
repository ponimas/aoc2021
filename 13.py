from pprint import pprint
from collections import defaultdict, deque
from itertools import groupby
from copy import deepcopy
from bisect import bisect_left

fname = "test.txt"
fname = "in/13.txt"


def fold_up(dots, line):
    keyfn = lambda x: x[1]

    dots.sort(key=keyfn)
    y = bisect_left(dots, line, key=keyfn)

    for i in range(y, len(dots)):
        dots[i] = (dots[i][0], (line - (dots[i][1] - line)))


def fold_left(dots, line):
    keyfn = lambda x: x[0]
    dots.sort(key=keyfn)

    x = bisect_left(dots, line, key=keyfn)

    for i in range(x, len(dots)):
        dots[i] = (line - (dots[i][0] - line), dots[i][1])


with open(fname) as f:
    dots = []
    while l := f.readline().strip():
        dots.append(tuple([int(x) for x in l.split(",")]))

    first = True
    while ins := f.readline().strip():
        ii, fld = ins.split("=")
        if ii.endswith("x"):
            fold_left(dots, int(fld))
        else:
            fold_up(dots, int(fld))

        if first:
            print(len(set(dots)))
            first = False

field = [
    ["." for _ in range(max(dots, key=lambda x: x[0])[0] + 1)]
    for _ in range(max(dots, key=lambda x: x[1])[1] + 1)
]

for x, y in dots:
    field[y][x] = "#"

for l in field:
    print("".join(l))
