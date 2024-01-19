from util import *
from .input import monkeys, modulus

rounds = 20

monkey_counts = [0]*len(monkeys)
for monkey in monkeys:
    monkey['items'] = list(monkey['starting'])

for _ in range(rounds):
    for i, monkey in enumerate(monkeys):
        for item in monkey['items']:
            monkey_counts[i] += 1
            item = monkey['op'](item)
            item //= 3
            item %= modulus
            monkey_target = monkey['test'][1] if monkey['test'][0](item) else monkey['test'][2]
            monkeys[monkey_target]['items'].append(item)
        monkey['items'] = []

monkey_counts.sort()
print(monkey_counts[-2] * monkey_counts[-1])