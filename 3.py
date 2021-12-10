from collections import Counter
from collections import deque
from copy import copy

# part 1
with open("in/3.txt") as inp:
    data = [x.strip() for x in inp]

l = len(data[0])

g = ""
e = ""
for i in range(l):
    x = Counter(x[i] for x in data)
    if x["1"] > x["0"]:
        g += "1"
        e += "0"
    else:
        g += "0"
        e += "1"

gamma = int(g, 2)
epsilon = int(e, 2)

print(gamma * epsilon)

o = copy(data)
c = copy(data)

for i in range(l):
    if len(o) == 1:
        break
    x = Counter(x[i] for x in o)

    if x["1"] < x["0"]:
        f = "0"
    else:
        f = "1"

    o = [x for x in o if x[i] == f]

for i in range(l):
    if len(c) == 1:
        break
    x = Counter(x[i] for x in c)

    if x["1"] < x["0"]:
        f = "1"
    else:
        f = "0"

    c = [x for x in c if x[i] == f]


print(int(o[0], 2) * int(c[0], 2))
