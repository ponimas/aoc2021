from itertools import *
from pprint import pprint
from math import *
from collections import *

fname = "test.txt"
# fname = "in/19.txt"

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


# def find_offset(p11, p12, p21, p22, skip):

#     for i, (dp21, dp22) in enumerate(zip(rotations(p21), rotations(p22))):

#         if i in skip:
#             continue

#         dp = sub(dp21, p11)
#         gp = add(p12, dp)

#         if gp == dp22:
#             return (i, dp)

#         dp = sub(dp22, p11)
#         gp = add(p12, dp)

#         if gp == dp21:
#             return (i, dp)

#     print(p11, p12, p21, p22)
#     return None, None


def find_offset(s1, s2):
    # BRUTEFORCE
    for p1, p2 in product(s1, s2):
        for idx, rp2 in enumerate(rotations(p2)):
            # guess that that's the point
            dp = sub(p1, rp2)
            dr2 = [rotations(p)[idx] for p in s2]
            ds2 = {add(p, dp) for p in dr2}

            over = set(s1) & set(ds2)

            if len(over) >= 12:
                print(over)
                return idx, point(dp.x * -1, dp.y * -1, dp.z * -1)


q = deque([0])

distances = [
    {distance(p1, p2): (p1, p2) for p1, p2 in combinations(s, 2)} for s in data
]


vv = set()

# for x in range(len(distances)):
#     for y in range(len(distances)):
#         xx, yy = sorted([x, y])

#         if xx == yy or (xx, yy) in vv:
#             continue

#         vv.add((xx, yy))

#         d1, d2 = distances[x], distances[y]
#         overlap = set(d1) & set(d2)

#         if len(overlap) >= 66:
#             print(x, y, len(overlap))


visited = set((a, b) for (a, b) in zip(range(len(data)), range(len(data))))


def transpose(p, i, dp):
    pr = rotations(p)[i]
    return sub(pr, dp)


while q:
    yy = q.popleft()
    s1 = distances[yy]

    for i in range(0, len(distances)):
        if (i, yy) in visited or (yy, i) in visited:
            continue

        visited.update([(i, yy), (yy, i)])

        s2 = distances[i]

        overlap = set(s1) & set(s2)

        if len(overlap) < 66:
            continue

        overlap_points_1 = set()
        overlap_points_2 = set()

        for k, v in s1.items():
            if k in overlap:
                overlap_points_1.update(v)

        for k, v in s2.items():
            if k in overlap:
                overlap_points_2.update(v)

        # skip = set()

        # for d in overlap:
        #     idx, dp = find_offset(*s1[d], *s2[d], skip)

        #     if idx is None:
        #         continue

        #     zz = {transpose(p, idx, dp) for p in overlap_points_2}

        #     if zz == overlap_points_1:
        #         break
        #     skip.add(idx)
        # else:
        #     continue

        idx, dp = find_offset(overlap_points_1, overlap_points_1)

        for ip, p in enumerate(data[i]):
            data[i][ip] = transpose(data[i][ip], idx, dp)

        # distances[i] = {
        #     distance(p1, p2): (p1, p2) for p1, p2 in combinations(data[i], 2)
        # }

        q.append(i)


points = set()

for s in data:
    for p in s:
        points.add(p)

pprint(len(points))
