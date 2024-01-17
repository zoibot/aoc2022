from util import *

total = 0
cycle = 0
def do_cycle():
    global cycle, total
    cycle += 1
    if (cycle - 20) % 40 == 0:
        total += cycle * x
x = 1
for inst in lines():
    if inst == 'noop':
        do_cycle()
    elif inst[:4] == 'addx':
        _, val = inst.split()
        do_cycle()
        do_cycle()
        x += int(val)

print(total)