import sys, os

day = sys.argv[1]
folder = 'day'+day.strip()

os.chdir(folder)

# TODO allow other parts
print('PART 1:')
__import__(folder+'.part1')

print('PART 2:')
__import__(folder+'.part2')
