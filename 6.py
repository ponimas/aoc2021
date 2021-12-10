from collections import Counter, defaultdict
from pprint import pprint

fname = "in/6.txt"
# fname = "test.txt"

with open(fname) as f:
    state = dict(Counter([int(i) for i in f.read().strip().split(",")]))

for _ in range(256):
    new = defaultdict(int)
    for i, c in state.items():
        if i == 0:
            new[8] = c
            new[6] += c
        else:
            new[i - 1] += c
    state = new

print(sum(state.values()))
