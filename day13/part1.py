from util import *

raw_pairs = (l.split('\n') for l in read().split('\n\n'))
pairs = [(eval(p[0]), eval(p[1])) for p in raw_pairs]

def compare(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            if left < right:
                return 1
            elif left > right:
                return -1
            else:
                return 0
        else:
            return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    else:
        for i in range(max(len(left), len(right))):
            if i >= len(left):
                return 1
            elif i >= len(right):
                return -1
            else:
                r = compare(left[i], right[i])
                if r == 0: continue
                return r
        return 0

total = 0
for i, (left, right) in enumerate(pairs, start=1):
    if compare(left, right) == 1:
        total += i

print(total)
