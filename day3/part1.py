t = 0
for sack in open('input').readlines():
    c = (set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])).pop()
    t += ord(c) - ord('A') + 27 if ord(c) < ord('a') else ord(c) - ord('a') + 1
print(t)