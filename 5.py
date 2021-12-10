from pprint import pprint
from collections import defaultdict

fname = "in/5.txt"
# fname = "test.txt"

field = defaultdict(int)
data = []

with open(fname) as d:
    for line in d:
        l, r = line.split(" -> ")
        x, y = l.split(",")
        a, b = r.split(",")
        x, y, a, b = int(x), int(y), int(a), int(b)
        data.append(((x, y), (a, b)))


with open(fname) as d:
    for (x, y), (a, b) in data:
        if x == a:
            s, e = sorted((y, b))
            for yy in range(s, e + 1):
                field[(x, yy)] += 1
        if y == b:
            s, e = sorted((x, a))
            for xx in range(s, e + 1):
                field[(xx, y)] += 1

print(len([1 for v in field.values() if v > 1]))


field = defaultdict(int)

with open(fname) as d:
    for (x, y), (a, b) in data:
        if x == a:
            s, e = sorted((y, b))
            for yy in range(s, e + 1):
                field[(x, yy)] += 1
        elif y == b:
            s, e = sorted((x, a))
            for xx in range(s, e + 1):
                field[(xx, y)] += 1
        else:
            if x < a:
                xs = range(x, a + 1)
            else:
                xs = range(x, a - 1, -1)

            if y < b:
                ys = range(y, b + 1)
            else:
                ys = range(y, b - 1, -1)

            for xx, yy in zip(xs, ys):
                field[(xx, yy)] += 1

print(len([1 for v in field.values() if v > 1]))
