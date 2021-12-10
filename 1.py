#!/usr/bin/env python3
import collections
import itertools


with open("in/1.txt") as inp:
    data = [int(l) for l in inp]

# part 1
cnt = 0
for d1, d2 in itertools.pairwise(data):
    if d2 > d1:
        cnt += 1

print(cnt)

# part 2
# from https://docs.python.org/3.10/library/itertools.html

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

cnt = 0

for a,b,c,d in sliding_window(data, 4):
    if sum([b, c, d]) > sum([a,b,c]):
        cnt +=1

print(cnt)
