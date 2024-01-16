from util import *


t = 0
for a, b, c in groupby(lines('input'), 3):
    badge = (set(a) & set(b) & set(c)).pop()
    t += ord(badge) - ord('A') + 27 if ord(badge) < ord('a') else ord(badge) - ord('a') + 1
print(t)