print(sum(sorted((sum(int(snack) for snack in elf.split('\n')) for elf in open('input').read().split('\n\n')), reverse=True)[:3]))
