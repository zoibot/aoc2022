s = open('input').read().strip()

for i in range(len(s)-13):
    if len(set(s[i:i+14])) == 14:
        print(i+14)
        break