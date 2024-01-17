import itertools
from dataclasses import dataclass

def lines(fname):
    return (line.strip() for line in open(fname).readlines())

def groupby(l, n):
    return iter(lambda: list(itertools.islice(iter(l), n)), [])

@dataclass
class Interval:
    lo: int
    hi: int

    def includes(self, n):
        return self.lo <= n and n <= self.hi
    def contains(self, other):
        return self.lo <= other.lo and self.hi >= other.hi
    def overlaps(self, other):
        return other.includes(self.lo) or other.includes(self.hi) or self.includes(other.lo) or self.includes(other.hi)

def transpose(g):
    return [[g[j][i] for j in range(len(g))] for i in range(len(g[0]))]

@dataclass #TODO
class Grid:
    cells: list

def parse_grid(fname):
    return transpose(list(lines(fname)))

def neighbors(x,y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
def bounded_neighbors(x,y,xmax,ymax):
    return [(x1,y1) for (x1,y1) in neighbors(x,y) if x >= 0 and x <= xmax and y >= 0 and y <= ymax]