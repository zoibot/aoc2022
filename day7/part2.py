from util import *

root = {}
cur = root

for line in lines('input'):
    if line[:4] == '$ cd':
        d = line[5:]
        if d == '/':
            cur = root
        else:
            if d not in cur:
                cur[d] = {}
                cur[d]['..'] = cur
            cur = cur[d]
    else:
        sz, name = line.split()
        if sz == 'dir' or sz == '$': continue
        cur[name] = int(sz)
        
dirsizes = {}
def size(node, path):
    if path in dirsizes:
        return dirsizes[path]
    cv = 0
    for entry, val in node.items():
        if entry == '..': continue
        if isinstance(val, int):
            cv += val
        else:
            cv += size(val, path+'/'+entry)
    dirsizes[path] = cv
    return cv
size(root, '')

need_to_delete = dirsizes[''] - 40000000
print(min(sz for sz in dirsizes.values() if sz >= need_to_delete))