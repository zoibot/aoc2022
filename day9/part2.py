from util import *

k = [(0,0)]*10

visited = set()
visited.add(k[-1])

for move in lines('input'):
    d, n = move.split()
    for _ in range(int(n)):
        if d == 'L':
            k[0] = (k[0][0]-1, k[0][1])
        elif d == 'R':
            k[0] = (k[0][0]+1, k[0][1])
        elif d == 'U':
            k[0] = (k[0][0], k[0][1]-1)
        elif d == 'D':
            k[0] = (k[0][0], k[0][1]+1)
        for i in range(1,10):
            delta = (k[i-1][0]-k[i][0], k[i-1][1]-k[i][1])
            kdelta = (delta[0]//abs(delta[0]) if abs(delta[0]) > 1 or (abs(delta[0]) == 1 and abs(delta[1]) > 1) else 0,
                    delta[1]//abs(delta[1]) if abs(delta[1]) > 1 or (abs(delta[1]) == 1 and abs(delta[0]) > 1) else 0)
            k[i] = (k[i][0] + kdelta[0], k[i][1] + kdelta[1])
        visited.add(k[-1])

print(len(visited))