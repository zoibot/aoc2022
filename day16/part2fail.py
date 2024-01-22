from util import *
from functools import lru_cache

rates = {}
tuns = {}
pos_rates = set()

for valve_spec in lines():
    sp = valve_spec.split()
    name = sp[1]
    rates[name] = int(sp[4][:-1].split('=')[1])
    if rates[name] > 0:
        pos_rates.add(name)
    tuns[name] = dict([(n[:2],1) for n in sp[9:]])

#TODO collapse graph... then have to deal with different distances...
collapsed = set()
for name, tsd in tuns.items():
    ts = list(tsd.keys())
    if rates[name] == 0 and len(ts) == 2:
        l = tsd[ts[0]] + tsd[ts[1]]
        del tuns[ts[0]][name]
        tuns[ts[0]][ts[1]] = l

        del tuns[ts[1]][name]
        tuns[ts[1]][ts[0]] = l
        collapsed.add(name)

for c in collapsed:
    del rates[c]
    del tuns[c]
print(tuns)


@lru_cache(maxsize=2**23)
def search(time, pos, pm, elepos, em, op):
    mm = min(em, pm)
    if mm > 0 and time > mm:
        em -= mm
        pm -= mm
        time -= mm

    if len(op) == 0 and time < 20:
        return 0

    if time == 0:
        return 0
    cur_rate = sum(rates[v] for v in op)
    if op == pos_rates:
        return cur_rate * time


    your_options = []
    if pm == 0: 
        if pos in pos_rates and pos not in op:
            your_options.append((pos, 0, [pos]))
        for tun, t in tuns[pos].items():
            your_options.append((tun, t-1, []))
    else:
        your_options.append((pos, pm-1, []))

    elephant_options = []
    if em == 0:
        if elepos in pos_rates and elepos not in op:
            elephant_options.append((elepos, 0, [elepos]))
        for tun, t in tuns[elepos].items():
            elephant_options.append((tun, t-1, []))
    else:
        elephant_options.append((elepos, em-1, []))


    options = []
    m = len(your_options)*len(elephant_options)
    i = 0
    for your_option in your_options:
        for elephant_option in elephant_options:
            if time == 26:
                i += 1
                print(i, '/', m)
            options.append(search(time-1,
                your_option[0], your_option[1],
                elephant_option[0], elephant_option[1],
                op.union(your_option[2] + elephant_option[2])))
    return cur_rate + max(options)

print(search(26, 'AA', 0, 'AA', 0, frozenset()))
