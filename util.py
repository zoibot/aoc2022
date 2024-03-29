import itertools
from dataclasses import dataclass

def init(f):
    global filen
    filen = f

def file(fname=None):
    fname = filen if fname is None else fname
    return open(fname)

def read(fname=None):
    return file(fname).read()

def lines(fname=None):
    return (line.strip() for line in file(fname).readlines())

def groupby(l, n):
    return iter(lambda: list(itertools.islice(iter(l), n)), [])

def line(start, end):
    x0, y0 = vec_or_tup(start)
    x1, y1 = vec_or_tup(end)
    if x0 == x1:
        for y in drange(y0, y1):
            yield Vec2(x0, y)
    elif y0 == y1:
        for x in drange(x0, x1):
            yield Vec2(x, y0)
    else:
        throw('no diagonal')

def drange(start, end):
    if start < end:
        return range(start, end+1)
    if end < start:
        return range(start, end-1, -1)

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
    def merge(self, other):
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

@dataclass
class IntervalSet:
    intervals: [Interval]

    def add(self, new):
        new_intervals = []
        adding = new
        for interval in self.intervals:
            if adding is None:
                new_intervals.append(interval)
            elif adding.overlaps(interval):
                adding = adding.merge(interval)
            elif adding.hi < interval.lo:
                new_intervals.append(adding)
                new_intervals.append(interval)
                adding = None
            elif adding.lo > interval.hi:
                new_intervals.append(interval)
        if adding is not None:
            new_intervals.append(adding)
        self.intervals = new_intervals
    
    def includes(self, n):
        return any(i.includes(n) for i in self.intervals)
    def contains(self, interval):
        return any(i.contains(interval) for i in self.intervals)




def transpose(g):
    return [[g[j][i] for j in range(len(g))] for i in range(len(g[0]))]

@dataclass
class Vec2:
    x: int
    y: int

    def __getitem__(self, i):
        return (self.x,self.y)[i]
    def __hash__(self):
        return (self.x, self.y).__hash__()
    def __add__(self, other):
        x, y = vec_or_tup(other)
        return Vec2(self.x + x, self.y + y)
    def __sub__(self, other):
        x, y = vec_or_tup(other)
        return Vec2(self.x - x, self.y - y)
    def __mul__(self, n):
        return Vec2(self.x * n, self.y * n)
    def mag(self):
        return math.sqrt(self.mag2())
    def mag2(self):
        return self.x ** 2 + self.y ** 2
    def manhattan(self):
        return abs(self.x) + abs(self.y)


def vec_or_tup(c):
    if isinstance(c, Vec2):
        x, y = c.x, c.y
    else:
        x, y = c
    return x, y

@dataclass
class Grid:
    cells: list

    def width(self):
        return len(self.cells[0])
    def height(self):
        return len(self.cells)
    def size(self):
        return (self.width(), self.height())
    def square(self):
        return self.width() == self.height()
    
    def find(self, cell):
        for y, r in enumerate(self.cells):
            for x, c in enumerate(r):
                if c == cell:
                    return (x,y)

    def findall(self, cell):
        for y, r in enumerate(self.cells):
            for x, c in enumerate(r):
                if c == cell:
                    yield (x,y)
    
    def __getitem__(self, c):
        x, y = vec_or_tup(c)
        return self.cells[y][x]

def parse_grid(fname):
    return Grid(list(lines(fname)))

def neighbors(c):
    x, y = vec_or_tup(c)
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
def bounded_neighbors(c, cmax):
    xmax, ymax = vec_or_tup(cmax)
    return [(x,y) for (x,y) in neighbors(c) if x >= 0 and x < xmax and y >= 0 and y < ymax]