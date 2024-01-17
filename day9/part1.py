from util import *

h = t = (0,0)

visited = set()
visited.add(t)

for move in lines('input'):
    d, n = move.split()
    for _ in range(int(n)):
        if d == 'L':
            h = (h[0]-1, h[1])
        elif d == 'R':
            h = (h[0]+1, h[1])
        elif d == 'U':
            h = (h[0], h[1]-1)
        elif d == 'D':
            h = (h[0], h[1]+1)
        delta = (h[0]-t[0], h[1]-t[1])
        tdelta = (delta[0]//abs(delta[0]) if abs(delta[0]) > 1 or (abs(delta[0]) == 1 and abs(delta[1]) > 1) else 0,
                  delta[1]//abs(delta[1]) if abs(delta[1]) > 1 or (abs(delta[1]) == 1 and abs(delta[0]) > 1) else 0)
        t = (t[0] + tdelta[0], t[1] + tdelta[1])
        visited.add(t)

print(len(visited))