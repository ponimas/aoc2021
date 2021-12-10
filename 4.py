from itertools import chain
from pprint import pprint
from collections import deque

fname = "in/4.txt"
# fname = "test.txt"

with open(fname) as inp:
    nums, *boards = inp.read().split("\n\n")

nums = nums.split(",")

boards = [
    [[x for x in l.strip().split()] for l in board.strip().split("\n")]
    for board in boards
]


def pivot(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def solve(boards):
    pboards = [pivot(board) for board in boards]
    winning = set(nums[:4])
    for i in range(4, len(nums)):
        winning.add(nums[i])
        for b, p in zip(boards, pboards):
            for line in chain(b, p):
                if winning.issuperset(line):
                    return nums[i], winning, b


class X(Exception):
    pass


def solve2(boards):
    pboards = [pivot(board) for board in boards]
    winning = set(nums[:4])
    for i in range(4, len(nums)):
        winning.add(nums[i])
        bb, pp = [], []

        for b, p in zip(boards, pboards):
            for line in chain(b, p):
                if winning.issuperset(line):
                    if len(boards) == 1:
                        return nums[i], winning, b
                    break
            else:
                bb.append(b)
                pp.append(p)
        boards, pboards = bb, pp


sum = 0
win, winning, board = solve(boards)
for i in chain.from_iterable(board):
    if i in winning:
        continue
    sum += int(i)

print(sum * int(win))

sum = 0
win, winning, board = solve2(boards)
for i in chain.from_iterable(board):
    if i in winning:
        continue
    sum += int(i)

print(sum * int(win))
