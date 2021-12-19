from operator import *
from functools import *
from collections import *
from pprint import pprint
from math import *
from itertools import *
from copy import deepcopy


fname = "test.txt"
fname = "in/18.txt"

with open(fname) as f:
    inp = [[int(x) if x.isdigit() else x for x in l.strip() if x != ","] for l in f]


def explode(l):
    d = 0
    i = 0

    while True:
        x = l[i]
        if x == "[":
            d += 1
        elif d >= 5:
            for ii in range(i - 1, 0, -1):
                if not isinstance(l[ii], int):
                    continue
                l[ii] += l[i]
                break

            for ii in range(i + 3, len(l)):
                if not isinstance(l[ii], int):
                    continue
                l[ii] += l[i + 1]
                break

            l[i - 1 : i + 3] = [0]
            return True

        elif x == "]":
            d -= 1

        i += 1

        if i == len(l):
            break

    return False


def split(l):
    for i in range(len(l)):
        x = l[i]
        if isinstance(x, int) and x > 9:
            l[i : i + 1] = ["[", floor(x / 2), ceil(x / 2), "]"]
            break


def freduce(l):
    ll = deepcopy(l)

    while explode(l):
        pass

    split(l)

    if l != ll:
        freduce(l)


def fprint(l):
    print(" ".join([str(x) for x in chain(l)]))


def plus(a, b):
    c = ["[", *a, *b, "]"]
    freduce(c)
    return c


def magnitude(l):
    i = 0
    while len(l) > 1:
        if (
            l[i] == "["
            and l[i + 3] == "]"
            and isinstance(l[i + 1], int)
            and isinstance(l[i + 2], int)
        ):
            l[i : i + 4] = [l[i + 1] * 3 + l[i + 2] * 2]
            i = 0
            break
        i += 1
    if len(l) == 1:
        return l[0]
    return magnitude(l)


s = reduce(plus, inp)
print(magnitude(s))

with open(fname) as f:
    inp = [[int(x) if x.isdigit() else x for x in l.strip() if x != ","] for l in f]

mp = 0

for a, b in permutations(inp, 2):
    a, b = deepcopy(a), deepcopy(b)
    c = plus(a, b)
    mp = max(mp, magnitude(c))


print(mp)
