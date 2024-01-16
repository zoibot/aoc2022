score = 0
for round in open('input').readlines():
    o, m = round.split()
    score += ' XYZ'.index(m)
    if (o == 'A' and m == 'Y') or (o == 'B' and m == 'Z') or (o == 'C' and m == 'X'):
        score += 6
    elif (o == 'A' and m == 'X') or (o == 'B' and m == 'Y') or (o == 'C' and m == 'Z'):
        score += 3
print(score)