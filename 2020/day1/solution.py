import os
stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n')
data = data[0:-1]

# part 1
target = 2020
for val in data:
    new_target = target-int(val)
    if str(new_target) in data:
        print(val, new_target, int(val)*new_target)
        break

# part 2
for val1 in data:
    for val2 in data:
        for val3 in data:
            if int(val1)+int(val2)+int(val3) == target:
                print(val1, val2, val3, int(val1)*int(val2)*int(val3))