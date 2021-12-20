from itertools import chain
from collections import Counter, defaultdict

fname = "test.txt"
fname = "in/20.txt"

trans = str.maketrans({".": "0", "#": "1"})

with open(fname) as f:
    alg, img = f.read().strip().split("\n\n")
    img = [i.strip() for i in img.split()]


def todict(img, default="."):
    dimg = defaultdict(lambda: default)
    for y, l in enumerate(img):
        for x, c in enumerate(l):
            dimg[(x, y)] = c
    return dimg


default = "."

for _ in range(50):
    new_img = []

    dimg = todict(img, default)
    for y in range(-1, len(img) + 1):
        new_line = []

        for x in range(-1, len(img[0]) + 1):
            dec = ""

            for yy in range(y - 1, y + 2):
                for xx in range(x - 1, x + 2):
                    dec += dimg[(xx, yy)]
            # print(dec)
            dec = dec.translate(trans)
            # print(dec)
            idx = int(dec, 2)

            # if x == 4 and y == 4:
            #     print("idx", dec, idx)
            new_line.append(alg[idx])

        new_img.append(new_line)
    default = new_img[-1][-1]
    img = new_img

cnt = Counter(chain(*img))
print(cnt["#"])
