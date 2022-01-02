from functools import lru_cache
from itertools import *
from pprint import pprint
from math import *
from collections import *
from heapq import *


fname = "test/19.txt"
fname = "in/19.txt"

point = namedtuple("point", ["x", "y", "z"])

with open(fname) as f:
    data = [
        [
            point(*[int(c) for c in line.strip().split(",")])
            for line in scanner.strip().split("\n")
            if not line.startswith("---")
        ]
        for _, scanner in enumerate(f.read().split("\n\n"))
    ]


def distance(p1, p2):
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2) + pow(p2.z - p1.z, 2))


@lru_cache
def rotations(p):
    x, y, z = p
    return [
        point(x, y, z),
        point(x, -y, -z),
        point(x, z, -y),
        point(x, -z, y),
        #
        point(-x, y, -z),
        point(-x, -y, z),
        point(-x, z, y),
        point(-x, -z, -y),
        #
        point(y, x, -z),
        point(y, -x, z),
        point(y, z, -x),
        point(y, -z, x),
        #
        point(-y, x, z),
        point(-y, -x, -z),
        point(-y, z, -x),
        point(-y, -z, x),
        #
        point(z, x, y),
        point(z, -x, -y),
        point(z, y, -x),
        point(z, -y, x),
        #
        point(-z, x, -y),
        point(-z, -x, y),
        point(-z, y, x),
        point(-z, -y, -x),
    ]


def add(p1, p2):
    return point(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z)


def sub(p1, p2):
    return point(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)


def find_offset(s1, s2):
    h = []

    # The bug is somewhere here

    for p1, p2 in product(s1, s2):

        for idx, rp2 in enumerate(rotations(p2)):

            dp = sub(p1, rp2)
            dr2 = (rotations(p)[idx] for p in s2)

            ds2 = {add(p, dp) for p in dr2}

            if len(ds2 & s1) >= 12:
                heappush(h, (-len(ds2 & s1), (idx, dp)))
    if len(h) > 0:
        _, x = heappop(h)
        return x

    print("That should not happen")
    return None, None

    # h = []

    # for p1, p2 in product(s1, s2):
    #     for idx, rp1 in enumerate(rotations(p1)):

    #         dp = sub(p2, rp1)
    #         dr1 = (rotations(p)[idx] for p in s1)

    #         ds1 = {add(p, dp) for p in dr1}

    #         if len(ds1 & s2) >= 12:
    #             heappush(h, (-len(ds1 & s2), (idx, point(-dp.x, -dp.y, -dp.z))))

    # if len(h) == 0:
    #     print("That should not happen")
    #     return None, None

    # _, x = heappop(h)
    # return x


distances = [
    {distance(p1, p2): (p1, p2) for p1, p2 in combinations(s, 2)} for s in data
]


visited = set()


def transpose(p, i, dp):
    pr = rotations(p)[i]
    return add(pr, dp)


def intersections(idx1, distances):
    s1 = distances[idx1]

    for idx2 in range(0, len(distances)):
        s2 = distances[idx2]

        if idx1 == idx2:
            continue
        if len(set(s1) & set(s2)) >= 66:
            yield idx1, idx2


q = deque(intersections(0, distances))

while q:
    idx1, idx2 = q.pop()

    if (idx1, idx2) in visited:
        continue

    visited.update({(idx2, idx1), (idx1, idx2)})

    s1 = distances[idx1]
    s2 = distances[idx2]

    overlap = set(s1) & set(s2)

    overlap_points_1 = {p for k, v in s1.items() for p in v if k in overlap}
    overlap_points_2 = {p for k, v in s2.items() for p in v if k in overlap}

    rotation, offset = find_offset(overlap_points_1, overlap_points_2)
    if rotation is None:
        continue

    for i in range(len(data[idx2])):
        data[idx2][i] = transpose(data[idx2][i], rotation, offset)

    distances[idx2] = {
        distance(p1, p2): (p1, p2) for p1, p2 in combinations(data[idx2], 2)
    }

    q.extend(intersections(idx2, distances))

points = {p for s in data for p in s}

"""
Wrong answers are:
- 465
- 543
- 573
- 585
"""

pprint(len(points))
