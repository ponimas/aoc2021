from itertools import cycle, count, combinations_with_replacement, product
from collections import defaultdict, Counter
from pprint import pprint

fname = "test.txt"
fname = "in/21.txt"

with open(fname) as f:
    f, s = f.read().strip().split("\n")

    _, f = f.split(":")
    _, s = s.split(":")

    f = int(f.strip())
    s = int(s.strip())


dice = zip(count(1), cycle(range(1, 101)))
triple_dice = zip(dice, dice, dice)

spaces = [f, s]


def move(pos, moves):
    rem = (pos + moves) % 10
    return 10 if rem == 0 else rem


scores = [0, 0]

while True:
    ((_, x1), (_, x2), (i, x3)) = next(triple_dice)

    spaces[0] = move(spaces[0], x1 + x2 + x3)
    scores[0] = scores[0] + spaces[0]

    if scores[0] >= 1000:
        print(scores[1] * i)
        break
    scores = [scores[1], scores[0]]
    spaces = [spaces[1], spaces[0]]


dice = list(sum(i) for i in product([1, 2, 3], [1, 2, 3], [1, 2, 3]))

print(Counter(dice))

dp = defaultdict(int)

dp[(0, 0, f, s)] = 1
scores = [0, 0]
idxs = cycle([0, 1])

while dp:
    i = next(idxs)
    ndp = defaultdict(int)

    while dp:
        state, cnt = dp.popitem()
        for d in dice:
            newstate = list(state)
            pos = move(newstate[2 + i], d)
            score = newstate[i] + pos

            if score >= 21:
                scores[i] += cnt

            else:
                newstate[2 + i] = pos
                newstate[i] = score
                ndp[tuple(newstate)] += cnt
    dp = ndp

print(scores)
