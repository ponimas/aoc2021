from pprint import pprint
from collections import defaultdict, deque
from itertools import groupby

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

pprint(map)

# The algorithm doesn't terminate.

deq = deque(["start"])

paths = defaultdict(set)

paths["start"] = {("start",)}

while deq:
    v = deq.pop()
    for p in paths[v]:

        for dv in map[v]:
            if dv.islower() and dv in p:
                continue

            track = (*p, dv)

            if track not in paths[dv]:
                paths[dv].add(track)
                deq.append(dv)

for p in sorted(paths["end"]):
    print(",".join(p))

print(len(paths["end"]))

deq = deque(["start"])
paths = defaultdict(set)
paths["start"] = {("start",)}


while deq:
    v = deq.pop()

    if v == "end":
        print(v, len(paths[v]))

    for p in paths[v]:
        for dv in map[v]:
            if (
                dv.islower()
                and dv in p
                and any(
                    len(list(cn)) > 1
                    for _, cn in groupby(filter(str.islower, sorted(p)))
                )
            ):
                continue

            track = (*p, dv)
            if track not in paths[dv]:
                paths[dv].add(track)
                deq.append(dv)


for p in sorted(paths["end"]):
    print(",".join(p))
print(len(paths["end"]))
