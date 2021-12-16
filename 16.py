from operator import *
from functools import *

fname = "test.txt"
fname = "in/16.txt"

with open(fname) as f:
    inp = ["".join(["{:b}".format(int(c, 16)).zfill(4) for c in l.strip()]) for l in f]


def read_literal(data):
    s = ""
    while True:
        b, data = data[:5], data[5:]
        s += b[1:]
        if b[0] == "0":
            break
    return int(s, 2), data


def parse(data):
    versions, data = int(data[:3], 2), data[3:]
    id, data = data[:3], data[3:]

    if id == "100":
        result, data = read_literal(data)

    else:
        length_type_id, data = data[0], data[1:]

        vals = []
        if length_type_id == "0":
            c, data = data[:15], data[15:]
            sub_packets_length = int(c, 2)
            subdata, data = data[:sub_packets_length], data[sub_packets_length:]

            while subdata:
                v, subdata, x = parse(subdata)
                versions += v
                vals.append(x)

        else:
            c, data = data[:11], data[11:]
            sub_packets_count = int(c, 2)

            for i in range(sub_packets_count):
                v, data, x = parse(data)
                versions += v
                vals.append(x)

        if id == "000":
            result = sum(vals)

        elif id == "001":
            result = reduce(mul, vals)

        elif id == "010":
            result = min(vals)

        elif id == "011":
            result = max(vals)

        elif id == "101":
            result = int(gt(*vals))
        elif id == "110":
            result = int(lt(*vals))
        elif id == "111":
            result = int(eq(*vals))

    return versions, data, result


# print(sum(parse(p)[0] for p in inp))
for p in inp:
    print(parse(p)[-1])
