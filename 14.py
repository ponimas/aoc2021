from pprint import pprint
from collections import *
from itertools import *

fname = "test.txt"
fname = "in/14.txt"

with open(fname) as f:
    inp = f.readline().strip()
    polymer = Counter(pairwise(inp))
    _ = f.readline()
    rules = {}
    for l in f:
        i, o = l.strip().split(" -> ")
        rules[tuple(i)] = o

pprint(dict(polymer))

for _ in range(40):
    new_polymer = defaultdict(int)
    for p, c in polymer.items():
        i = rules[p]
        new_polymer[(p[0], i)] += c
        new_polymer[(i, p[1])] += c
    polymer = new_polymer

c = defaultdict(int)

for p, i in polymer.items():
    c[p[0]] += i
    c[p[1]] += i

c[inp[0]] += 1
c[inp[-1]] += 1

cmn = Counter(c).most_common()

print((cmn[0][1] - cmn[-1][1]) // 2)
