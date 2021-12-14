from pprint import pprint
from collections import *
from itertools import *
import numpy as np


# from copy import deepcopy
# from bisect import bisect_left

fname = "test.txt"
# fname = "in/14.txt"

with open(fname) as f:
    polymer = np.array([ord(x) for x in f.readline().strip()])
    _ = f.readline()
    rules = {}
    for l in f:
        i, o = l.strip().split(" -> ")
        rules[tuple([ord(x) for x in i])] = ord(o)

# pprint(rules)

for _ in range(40):
    new_polymer = np.empty(polymer.size * 2 - 1, dtype=polymer.dtype)
    for i, pair in enumerate(pairwise(polymer)):
        new_polymer[i * 2] = polymer[i]
        new_polymer[i * 2 + 1] = rules[pair]
    new_polymer[-1] = polymer[-1]
    # print(new_polymer)
    polymer = new_polymer

c = Counter(polymer).most_common()
# print(c)

print(c[0][1] - c[-1][1])
