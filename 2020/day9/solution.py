import os
import re
stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n')[:-1]

preamble = 25
target = None
# PART 1
for idx,num in enumerate(data):
    if idx <= preamble-1:
        continue

    flag = 0
    for v1 in data[idx-preamble:idx]:
        for v2 in data[idx-preamble:idx]:
            if int(v1)+int(v2)==int(num):
                flag=1

    if flag==0:
        target = int(num)
        print('Part 1:', num)
        break

# PART 2
number_list = []
sum = 0
for idx,val1 in enumerate(data):
    number_list.append(int(val1))
    sum = int(val1)
    for val2 in data[idx+1:]:
        sum+=int(val2)
        number_list.append(int(val2))
        if sum==target:
            print('PART 2:', min(number_list)+max(number_list))
            break
    number_list = []
    sum = 0
