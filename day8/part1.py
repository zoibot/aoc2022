from util import *

g = parse_grid('input')
visible = set()

for x in range(1,g.width()-1):
    curmax = g[(x,0)]
    visible.add((x,0))
    for y in range(1, g.height()):
        if g[x,y] > curmax:
            curmax = g[x,y]
            visible.add((x,y))
    curmax = g[x,g.height()-1]
    visible.add((x, g.height()-1))
    for y in range(g.height()-1, 0, -1):
        if g[x,y] > curmax:
            curmax = g[x,y]
            visible.add((x,y))
        

for y in range(1,g.height()-1):
    curmax = g[0,y]
    visible.add((0, y))
    for x in range(1, g.width()):
        if g[x,y] > curmax:
            curmax = g[x,y]
            visible.add((x,y))
    curmax = g[g.width()-1,y]
    visible.add((g.width()-1, y))
    for x in range(g.width()-1, 0, -1):
        if g[x,y] > curmax:
            curmax = g[x,y]
            visible.add((x,y))
        
print(len(visible)+4) # +4 for corners
            
