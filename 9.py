import itertools
from functools import lru_cache
from pprint import pprint
from collections import defaultdict

fname = "in/9.txt"
# fname = "test.txt"

data = []
with open(fname) as inp:
    for l in inp:
        data.append([int(x) for x in l.strip()])

lx = len(data[0])
ly = len(data)


@lru_cache(maxsize=102400)
def neighbours(x, y):
    return [
        (xi, yi)
        for xi, yi in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if xi >= 0 and yi >= 0 and xi < lx and yi < ly
    ]


lowpoints = []

for y, l in enumerate(data):
    for x, i in enumerate(l):
        ns = neighbours(x, y)
        if all(data[ny][nx] > i for nx, ny in ns):
            lowpoints.append(i)


print(sum(x + 1 for x in lowpoints))

basins_map = [[-1 for _ in l] for l in data]
basins = defaultdict(set)

BOLD = "\033[1m"
END = "\033[0m"


def print_map():
    m = []
    for y in range(0, ly):
        l = []
        for x in range(0, lx):
            if basins_map[y][x] != -1:
                l.append(BOLD + str(data[y][x]) + END)
            else:
                l.append(str(data[y][x]))

        m.append("".join(l))
    # print("\n".join(m))
    mm = []

    for y in range(0, ly):
        mm.append(
            ",".join(
                [BOLD + chr(i + 220) + END if i > -1 else "9" for i in basins_map[y]]
            )
        )

    print("\n".join(mm))


k = 0


def next_basin():
    ks = basins.keys()
    if not len(ks):
        return 0
    return max(ks) + 1


def update(i, ps):
    for (x, y) in ps:
        basins_map[y][x] = i
    basins[i].update(ps)


def find_basin(x, y):
    # ns = [
    #     (nnx, nny)
    #     for nx, ny in neighbours(x, y)
    #     for nnx, nny in neighbours(nx, ny)
    #     if data[ny][nx] != 9 and data[nny][nnx] != 9
    # ]

    ns = [(nx, ny) for nx, ny in neighbours(x, y) if data[ny][nx] != 9]
    bs = sorted([basins_map[ny][nx] for nx, ny in ns if basins_map[ny][nx] != -1])

    if not bs:
        bm = next_basin()
        update(bm, [(x, y), *ns])
        return
    else:
        z = bs[0]
        update(z, [(x, y), *ns])
        for bm in bs[1:]:
            update(z, basins[bm])

    # if (x, y) in [(12, 7), (12, 8)]:
    #     print_map()
    #     print()


for x, y in itertools.product(range(0, lx), range(0, ly)):
    i = data[y][x]
    if i != 9:
        find_basin(x, y)


# print_map()
b = [len(x) for x in basins.values()]
b.sort()

a = 1
for l in b[-3:]:
    a *= l

print(a)
# print(b)
1012828
1330560
