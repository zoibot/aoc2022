s = open('input').read().strip()

for i in range(len(s)-3):
    if len(set(s[i:i+4])) == 4:
        print(i+4)
        break