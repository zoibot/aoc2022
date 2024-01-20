from util import *

g = Grid(list(lines())) # TODO make grid auto read

start = g.find('S')
end = g.find('E')

d = {start: 0}

q = [start]
while len(q) > 0:
    c = q.pop(0)
    if c == end:
        break
    l = d[c]
    h = g[c]
    if h == 'S': h = 'a'
    if h == 'E': h = 'z'
    for n in bounded_neighbors(c, g.size()):
        if n in d and d[n] <= l+1:
            continue
        nh = g[n]

        if ord(nh) - ord(h) > 1:
            continue
        d[n] = l+1
        q.append(n)

print(d[end])