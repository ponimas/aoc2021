from pprint import pprint

BOLD = "\033[1m"
END = "\033[0m"
ZERO = BOLD + "0" + END

fname = "test.txt"
fname = "in/11.txt"


def pretty(field):
    for l in field:
        p = ""
        for s in l:
            if s == 0:
                p += ZERO
            else:
                p += str(s)
        print(p)


def neigbours(x, y):
    for dx in range(x - 1, x + 2):
        if dx < 0 or dx > 9:
            continue
        for dy in range(y - 1, y + 2):
            if dy < 0 or dy > 9:
                continue
            if dx == x and dy == y:
                continue
            yield dx, dy


def glow(field, glowing, x, y):
    if (x, y) in glowing:
        return

    elif field[y][x] == 9:
        field[y][x] = 0
        glowing.add((x, y))
        for nx, ny in neigbours(x, y):
            glow(field, glowing, nx, ny)
    else:
        field[y][x] += 1


def step(field):
    glowing = set()
    for y, l in enumerate(field):
        for x, _ in enumerate(l):
            glow(field, glowing, x, y)
    return glowing
    # pretty(field)


with open(fname) as f:
    oct = [[int(i) for i in l.strip()] for l in f]


total = 0
for _ in range(100):

    g = step(oct)
    total += len(g)
print(total)

with open(fname) as f:
    oct = [[int(i) for i in l.strip()] for l in f]

i = 0
while 1:
    i += 1
    g = step(oct)
    if len(g) == 100:
        print(i)
        break
