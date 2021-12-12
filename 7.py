from collections import defaultdict
from pprint import pprint
from functools import lru_cache


BOLD = "\033[1m"
END = "\033[0m"

fname = "test.txt"
fname = "in/7.txt"

with open(fname) as f:
    inp = [int(x) for x in f.readline().strip().split(",")]

fuel = defaultdict(int)

for p in range(0, max(inp) + 1):
    for i in inp:
        fuel[p] += abs(i - p)

# print(fuel)
fuel = list(fuel.items())

# print(fuel)
fuel.sort(key=lambda x: x[1])

pprint(fuel[:1])


fuel = defaultdict(int)


def f(x):
    if x % 2 == 0:
        return (x + 1) * x // 2
    else:
        return (x + 1) * (x // 2) + (x // 2 + 1)


for p in range(0, max(inp) + 1):
    for i in inp:
        fuel[p] += f(abs(i - p))

fuel = list(fuel.items())
# print(fuel)
fuel.sort(key=lambda x: x[1])

pprint(fuel[:1])
