from dataclasses import dataclass
from collections import namedtuple
from pprint import pprint

fname = "test.txt"
# fname = "in/22.txt"


@dataclass
class coord:
    x: int
    y: int
    z: int


@dataclass
class cube:
    bl: coord
    tr: coord

    def overlap(self, other):
        if not (
            self.bl.x > other.tr.x
            or self.bl.y > other.tr.y
            or self.bl.z > other.tr.z
            or self.tr.x < other.bl.x
            or self.tr.y < other.bl.y
            or self.tr.z < other.bl.z
        ):
            return cube(
                coord(
                    max(self.bl.x, other.bl.x),
                    max(self.bl.y, other.bl.y),
                    max(self.bl.z, other.bl.z),
                ),
                coord(
                    min(self.tr.x, other.tr.x),
                    min(self.tr.y, other.tr.y),
                    min(self.tr.z, other.tr.z),
                ),
            )

    def volume(self):
        # assuming it's a cube
        return (
            (self.tr.x - self.bl.x + 1)
            * (self.tr.y - self.bl.y + 1)
            * (self.tr.z - self.bl.z + 1)
        )


with open(fname) as f:
    instructions = []
    for l in f:
        inst, cc = l.strip().split(" ")
        coords = [[int(p) for p in c[2:].split("..")] for c in cc.split(",")]

        instructions.append(
            (
                inst,
                cube(
                    coord(coords[0][0], coords[1][0], coords[2][0]),
                    coord(coords[0][1], coords[1][1], coords[2][1]),
                ),
            )
        )

# bounds = [[-50, 50], [-50, 50], [-50, 50]]

# on = set()
# for inst, coords in instructions:
#     coords = {
#         (x, y, z)
#         for x in range(max(-50, coords[0][0]), min(50, coords[0][1]) + 1)
#         for y in range(max(-50, coords[1][0]), min(50, coords[1][1]) + 1)
#         for z in range(max(-50, coords[2][0]), min(50, coords[2][1]) + 1)
#     }

#     if inst == "on":
#         on.update(coords)
#     else:
#         on -= coords


# def overlap(c1, c2):
#     if c1[0].x >  c2[1].


on = []
off = []

for command, c in instructions:
    v = c.volume()

    if command == "on":
        on.append(c)
        for

        for o in off:
            if n := c.overlap(o):
                on.append(n)
    else:
        # off.append(c)
        for o in on:
            if n := c.overlap(o):
                off.append(n)
volume = 0

for o in on:
    volume += o.volume()

for o in off:
    volume -= o.volume()

pprint(on)
pprint(off)
