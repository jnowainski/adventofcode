import os

stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')
data = stream.read().split('\n')[0:-1]

def run(iv_pairs):
    accumulator = 0
    visited = [0]*len(iv_pairs)
    instruction_ctr = 0 

    while True:
        if instruction_ctr>=len(iv_pairs):
            print('True', accumulator)
            return True
        if visited[instruction_ctr]:
            return False

        visited[instruction_ctr] = 1
        ins = iv_pairs[instruction_ctr][0]
        val = iv_pairs[instruction_ctr][1]

        if ins =='nop':
            instruction_ctr += 1
            continue
        elif ins=='acc':
            accumulator+= int(val)
            instruction_ctr += 1
        elif ins=='jmp':
            instruction_ctr += int(val)

# PART 1
accumulator = 0
visited = [0]*len(data)
instruction_ctr = 0
while visited[instruction_ctr] != 1:
    visited[instruction_ctr] = 1

    instruction = data[instruction_ctr].split(' ')[0]
    val = data[instruction_ctr].split(' ')[1]

    if instruction=='nop':
        instruction_ctr += 1
        continue
    elif instruction=='acc':
        accumulator+= int(val)
        instruction_ctr += 1
    elif instruction=='jmp':
        instruction_ctr += int(val)

print('PART 1: ', accumulator)

# PART 2
iv_pairs = []
for iv in data:
    i = iv.split(' ')[0]
    v = iv.split(' ')[1]
    iv_pairs.append([i,v])

iv_original = iv_pairs

replace_max = 0
while True:
    if not run(iv_pairs):
        print('No success', replace_max)
        replace_ctr = 0
        iv_pairs = iv_original
        for idx,iv in enumerate(iv_pairs):
            if iv[0]=='nop' or iv[0]=='jmp':
                if replace_ctr == replace_max:
                    print('replace')
                    if iv[0]=='nop': iv_pairs[idx][0] = 'jmp'
                    else: iv_pairs[idx][0] = 'nop'
                    replace_max+=1
                    break
                replace_ctr+=1

    else:
        print('PART 2 Done')
        break
