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

    def contains(other):
        return lo <= other.lo and hi >= other.hi
    
