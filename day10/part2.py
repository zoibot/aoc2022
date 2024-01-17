from util import *

crt = ''
cycle = 0
x = 1
def do_cycle():
    global cycle, crt
    if abs(cycle % 40 - x) <= 1:
        crt += '#'
    else:
        crt += '.'
    cycle += 1
    if cycle % 40 == 0:
        crt += '\n'

for inst in lines():
    if inst == 'noop':
        do_cycle()
    elif inst[:4] == 'addx':
        _, val = inst.split()
        do_cycle()
        do_cycle()
        x += int(val)

print(crt)