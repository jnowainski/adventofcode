import os
stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n')[0:-1]

r = 0
d = 0
r_add = 1   # this will determine the steps to the right side
d_add = 2   # this will determine the steps downwards
max_r = len(data[0])
max_d = len(data)
tree = '#'

tree_counter = 0

for v in data:
    position = data[d][r]
    if position==tree:
        tree_counter+=1

    r=(r+r_add)%max_r
    if d>=max_d-1:
        print(tree_counter, r_add, d_add)
        break
    else:
        d+=d_add

