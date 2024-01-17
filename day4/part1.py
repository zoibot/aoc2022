from util import *

c = 0
for l in lines('input'):
    r1, r2 = (Interval(*(int(b) for b in r.split('-'))) for r in l.split(','))
    if r1.contains(r2) or r2.contains(r1):
        c += 1

print(c)