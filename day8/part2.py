from util import *

g = parse_grid('input')
visible = set()

best = 0

for x in range(0,len(g[0])):
    for y in range(0,len(g)):
        h = g[x][y]
        # left
        l = 0
        for i in range(x):
            l += 1
            if g[x-i-1][y] >= h:
                break
        # right
        r = 0
        for i in range(len(g)-x-1):
            r += 1
            if g[x+i+1][y] >= h:
                break
        # up
        u = 0
        for i in range(y):
            u += 1
            if g[x][y-i-1] >= h:
                break
        # down
        d = 0
        for i in range(len(g)-y-1):
            d += 1
            if g[x][y+i+1] >= h:
                break
        score = l * r * u * d
        if score > best:
            best = score

print(best)
            
