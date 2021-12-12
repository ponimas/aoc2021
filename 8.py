from itertools import chain
from collections import defaultdict, deque
from pprint import pprint
from functools import lru_cache

fname = "test.txt"
fname = "in/8.txt"

n1 = 2
n4 = 4
n7 = 3
n8 = 7

with open(fname) as f:
    data = [l.split(" | ")[1].split() for l in f]

cnt = 0

for d in chain(*data):
    cnt += len(d) in {n1, n4, n7, n8}

print(cnt)


with open(fname) as f:
    data = [
        [["".join(sorted(y)) for y in x.split()] for x in l.strip().split(" | ")]
        for l in f
    ]

total = 0
for l, r in data:
    digi = [None for _ in range(10)]
    s = sorted(list(set([*l, *r])), key=lambda x: len(x))
    z = deque([set(x) for x in s])

    while len(z):
        x = z.popleft()

        if len(x) == n1:
            digi[1] = x
            continue

        elif len(x) == n4:
            digi[4] = x
            continue

        elif len(x) == n7:
            digi[7] = x
            continue

        elif len(x) == n8:
            digi[8] = x
            continue

        elif (
            len(x) == 5
            and not digi[3]
            and digi[7]
            and x.issuperset(digi[7])
            and len(x - digi[7]) == 2
        ):
            digi[3] = x

        elif (
            len(x) == 6
            and not digi[9]
            and digi[3]
            and x.issuperset(digi[3])
            and len(x - digi[3]) == 1
        ):
            digi[9] = x

        elif (
            len(x) == 6
            and not (digi[0] and digi[6])
            and digi[8]
            and digi[9]
            and len(digi[8] - x) == 1
        ):
            if len(digi[1] - x) == 0:
                digi[0] = x
            elif len(digi[1] - x) == 1:
                digi[6] = x

        elif len(x) == 5 and not (digi[5] and digi[2]) and digi[6]:
            if not digi[6].issuperset(x):
                digi[2] = x
            elif digi[6].issuperset(x) and len(digi[6] - x) == 1:
                digi[5] = x
        else:
            z.append(x)

    m = {"".join(sorted(list(d))): n for n, d in enumerate(digi)}
    total += int("".join(str(m[x]) for x in r))

print(total)
