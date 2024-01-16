score = 0
plays = 'ABC'
for round in open('input').readlines():
    o, m = round.split()
    i = plays.index(o)
    if m == 'X':
        score += (i-1)%3+1
    elif m == 'Y':
        score += i+1
        score += 3
    elif m == 'Z':
        score += (i+1)%3+1
        score += 6
print(score)