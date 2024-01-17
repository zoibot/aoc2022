import sys, os
import util

day = sys.argv[1]
file = 'input' # TODO
if len(sys.argv) > 2:
    file = sys.argv[2]
util.init(file)
folder = 'day'+day.strip()

os.chdir(folder)

# TODO allow other parts
print('PART 1:')
__import__(folder+'.part1')

print('PART 2:')
__import__(folder+'.part2')
