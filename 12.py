from pprint import pprint
from collections import defaultdict, deque, Counter
from itertools import groupby
from copy import deepcopy

fname = "test.txt"
fname = "in/12.txt"

map = defaultdict(list)

with open(fname) as f:
    for l in f:
        s, e = l.strip().split("-")

        if s != "end" and e != "start":
            map[s].append(e)

        if e != "end" and s != "start":
            map[e].append(s)

deq = deque(
    [
        [
            "start",
        ]
    ]
)


paths = []

while deq:
    path = deq.pop()

    for v in map[path[-1]]:
        if v == "end":
            paths.append([*path, v])
            continue

        if v.islower() and len([x for x in path if x == v]) > 0:
            continue

        deq.append([*path, v])

print(len(paths))


deq = deque(
    [
        [
            "start",
        ]
    ]
)


paths = []

while deq:
    path = deq.pop()
    for v in map[path[-1]]:
        if v == "end":
            paths.append([*path, v])
            continue
        new_path = [*path, v]

        if v.islower():
            lower = Counter([x for x in new_path if x.islower()])
            if len([1 for _, v in lower.items() if v > 1]) > 1 or any(
                1 for _, v in lower.items() if v > 2
            ):
                continue

        deq.append(new_path)

print(len(paths))
