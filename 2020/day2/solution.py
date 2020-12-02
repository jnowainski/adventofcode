import os
stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n')
counter = 0

# part 1
for pw in data:
    if pw == '':
        break

    pw_split = pw.split(' ')  
    policy_char = pw_split[1].split(':')[0]
    policy_val = pw_split[0].split('-')

    # check policy
    num_char = pw_split[2].count(policy_char)
    if num_char >= int(policy_val[0]) and num_char <= int(policy_val[1]):
        counter += 1

print('Part 1: ', counter)


# part 2
counter = 0
for pw in data:
    if pw == '':
        break

    pw_split = pw.split(' ')  
    policy_char = pw_split[1].split(':')[0]
    policy_val = pw_split[0].split('-')

    # check policy
    chars = pw_split[2][int(policy_val[0])-1]+pw_split[2][int(policy_val[1])-1]
    
    if chars.count(policy_char) == 1:
        counter += 1

print('Part 2: ',counter)
