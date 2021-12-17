from operator import *
from functools import *
from collections import *
from math import *
from itertools import *
import re

fname = "test.txt"
fname = "in/17.txt"

coord = namedtuple("coord", ["x", "y"])

with open(fname) as f:
    l = f.readline().strip()
    tg = [
        int(i)
        for i in re.match("^target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)$", l).groups()
    ]


def step(pos, velocity, tg):
    # print(pos, velocity)
    if tg[0] <= pos.x <= tg[1] and tg[2] <= pos.y <= tg[3]:
        return None, None, True

    elif pos.x > tg[1]:
        return None, None, None

    elif tg[2] > pos.y:
        return None, None, None

    d_pos = coord(pos.x + velocity.x, pos.y + velocity.y)

    if velocity.x > 0:
        d_vx = velocity.x - 1
    elif velocity.x < 0:
        d_vx = velocity.x + 1
    else:
        d_vx = 0

    return d_pos, coord(d_vx, velocity.y - 1), None


ys = max([abs(tg[2]), abs(tg[3])])
velocity = coord(ceil(sqrt(2 * tg[0])), ys)

pos = coord(0, 0)
m = 0

print(velocity, tg)

while True:
    pos, velocity, _ = step(pos, velocity, tg)
    if not pos:
        print("DONE", m)
        break
    if pos.y > m:
        m = pos.y


ys = max([abs(tg[2]), abs(tg[3])])
ins = []

for x, y in product(
    range(1, tg[1] + 2),
    range(-ys, ys + 1),
):
    pos = coord(0, 0)
    velocity = coord(x, y)

    while True:
        pos, velocity, i = step(pos, velocity, tg)
        if i:
            ins.append((x, y))
        if not pos:
            break

# print(ins)
print("DONE", len(ins))
