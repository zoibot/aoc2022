from util import *
from functools import cache

rates = {}
tuns = {}
pos_rates = set()

for valve_spec in lines():
    sp = valve_spec.split()
    name = sp[1]
    rates[name] = int(sp[4][:-1].split('=')[1])
    if rates[name] > 0:
        pos_rates.add(name)
    tuns[name] = [n[:2] for n in sp[9:]]

@cache
def search(time, pos, op):
    if time == 0:
        return 0
    cur_rate = sum(rates[v] for v in op)
    if op == pos_rates:
        return cur_rate * time
    options = []
    if rates[pos] > 0 and pos not in op:
        open_valve = search(time-1, pos, op.union([pos]))
        options.append(open_valve)
    for tun in tuns[pos]:
        options.append(search(time-1, tun, op))
    return cur_rate + max(options)

print(search(30, 'AA', frozenset()))
