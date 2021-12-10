# part 1

depth = 0
pos = 0

with open("in/2.txt") as inp:
    for c in inp:
        match c.split():
           case ["forward", x]:
               pos += int(x)
           case ["up", x]:
               depth -= int(x)
           case ["down", x]:
               depth += int(x)

print(depth*pos)


# part 2

depth = 0
pos = 0
aim = 0

with open("in/2.txt") as inp:
    for c in inp:
        match c.split():
           case ["forward", x]:
               pos += int(x)
               depth += aim * int(x)
           case ["up", x]:
               aim -= int(x)
           case ["down", x]:
               aim += int(x)

print(depth*pos)
