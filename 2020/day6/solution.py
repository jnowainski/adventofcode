import os

stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')
data = stream.read().split('\n\n')

# PART 1
sum = 0
for group in data:
    set = {*group.replace('\n','')}
    sum += len(set)

print('PART 1: ',sum)

# PART 2
sum = 0
for group in data:
    sets = [{*s} for s in group.split('\n') if s]
    sum += len(sets[0].intersection(*sets))

print('PART 2: ',sum)