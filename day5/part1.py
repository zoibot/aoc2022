fl = open('input').read()
raw_crates, raw_instructions = fl.split('\n\n')
crate_lines = raw_crates.split('\n')
stacks = [[] for _ in range((len(crate_lines[0])+1) // 4)]

for layer in reversed(crate_lines[:-1]):
    for i, stack in enumerate(stacks):
        c = layer[i*4+1]
        if c != ' ': stack.append(c)

for inst in raw_instructions.split('\n'):
    _, ct, _, src, _, dest = inst.split()
    ct, src, dest = int(ct), int(src), int(dest)
    for _ in range(ct):
        c = stacks[src-1].pop()
        stacks[dest-1].append(c)

print(''.join(stack[-1] for stack in stacks))
