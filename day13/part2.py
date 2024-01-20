from functools import cmp_to_key

from util import *

packets = [[[6]],[[2]]]
for l in lines():
    if l != '':
        packets.append(eval(l))

def compare(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return 1
            else:
                return 0
        else:
            return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    else:
        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return -1
            elif i >= len(right):
                return 1
            else:
                r = compare(left[i], right[i])
                if r == 0: continue
                return r
        return 0

packets.sort(key=cmp_to_key(compare))

print((packets.index([[6]])+1) * (packets.index([[2]])+1))
