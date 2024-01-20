from util import *

g = Grid(list(lines())) # TODO make grid auto read

end = g.find('E')

starts = list(g.findall('a')) + [g.find('S')]

ds = []
for start in starts: # TODO this is the lazy way of doing this by reusing part 1. 
                     # Could calculate all at once by searching from E to all spaces.
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
    if end in d:
        ds.append(d[end])

print(min(ds))