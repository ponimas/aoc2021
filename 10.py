from collections import deque
from pprint import pprint

fname = "in/10.txt"
# fname = "test.txt"


points_corruption = 0


incomplete = []

def check_line(l):
    global points_corruption

    d = deque()
    for c in l:
        if c in {"]",")","}",">"}:
            p = d.pop()
            match (p, c):
                case ["(", ")"]|["{","}"]|["[","]"]|["<",">"]:
                    continue
            match c:
               case ")":
                   points_corruption += 3
               case "]":
                   points_corruption += 57
               case "}":
                   points_corruption += 1197
               case ">":
                   points_corruption += 25137
            return
        else:
            d.append(c)
    if len(d):
        incomplete.append(d)

def complete(l):
    points = 0
    for c in reversed(l):
        points *= 5
        match c:
           case "(":
               points += 1
           case "[":
               points += 2
           case "{":
               points += 3
           case "<":
               points += 4
    return points


with open(fname) as f:
    for l in f:
        check_line(l.strip())

print(points_corruption)

incomplete_scores = [complete(l) for l in incomplete]

pprint(sorted(incomplete_scores)[len(incomplete_scores)//2])
