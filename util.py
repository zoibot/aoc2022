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
