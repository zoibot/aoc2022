from util import *

grid = set()

for path in lines():
    pts = [[int(x) for x in pt.split(',')] for pt in path.split(' -> ')]
    for i in range(len(pts)-1):
        grid.update(line(pts[i], pts[i+1]))

maxy = max(p.y for p in grid)

sand_origin = (500,0)

sand_at_rest = 0
done = False
while not done:
    sand = Vec2(*sand_origin)
    if sand in grid:
        break
    while True:
        if sand.y == maxy+1: 
            sand_at_rest += 1
            grid.add(sand)
            break

        if (sand + (0, 1)) not in grid:
            sand += (0, 1)
        elif (sand + (-1, 1)) not in grid:
            sand += (-1, 1)
        elif (sand + (1, 1)) not in grid:
            sand += (1, 1)
        else:
            sand_at_rest += 1
            grid.add(sand)
            break

print(sand_at_rest)
