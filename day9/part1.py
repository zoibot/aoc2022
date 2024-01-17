from util import *

h = t = Vec2(0,0)

visited = set()
visited.add(t)

for move in lines('input'):
    d, n = move.split()
    for _ in range(int(n)):
        if d == 'L':
            h -= (1, 0)
        elif d == 'R':
            h += (1, 0)
        elif d == 'U':
            h -= (0, 1)
        elif d == 'D':
            h += (0, 1)
        delta = h-t
        tdelta = Vec2(delta[0]//abs(delta[0]) if abs(delta[0]) > 1 or (abs(delta[0]) == 1 and abs(delta[1]) > 1) else 0,
                  delta[1]//abs(delta[1]) if abs(delta[1]) > 1 or (abs(delta[1]) == 1 and abs(delta[0]) > 1) else 0)
        t += tdelta
        visited.add(t)

print(len(visited))