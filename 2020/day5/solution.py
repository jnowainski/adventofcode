import os
from math import ceil
stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n')[:-1]   # drop empty row

def decode_plane_row(code, code_id, range):
    # endergebnis
    if range[1]-range[0]==1:
        if code[code_id] == 'F':
            return range[0]
        else:
            return range[1]
    
    # ansonsten, splitte range
    if code[code_id] == 'F':
        range = (range[0], range[0]+(range[1]-range[0])//2)
        return decode_plane_row(code, code_id+1, range)
    else:
        range = (range[0]+ceil((range[1]-range[0])/2), range[1])
        return decode_plane_row(code, code_id+1, range)

def decode_plane_seat(code, code_id, range):
    # endergebnis
    if range[1]-range[0]==1:
        if code[code_id] == 'L':
            return range[0]
        else:
            return range[1]
    
    # ansonsten, splitte range
    if code[code_id] == 'L':
        range = (range[0], range[0]+(range[1]-range[0])//2)
        return decode_plane_row(code, code_id+1, range)
    else:
        range = (range[0]+ceil((range[1]-range[0])/2), range[1])
        return decode_plane_row(code, code_id+1, range)

# PART 1
seat_list = []
for i in data:
    row = decode_plane_row(i[:-3], 0, (0,127))
    seat = decode_plane_seat(i[-3:], 0, (0,7))
    id = row*8+seat
    seat_list.append(int(id))
print('PART 1: ', max(seat_list))


seat_ids = []

for seat in data:
    row = int(seat[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(seat[-3:].replace('R', '1').replace('L', '0'), 2)
    seat_ids.append(row * 8 + col)

# PART 2
seat_ids = sorted(seat_ids)
last_seat = None
for seat in seat_ids:
    if last_seat and seat - last_seat == 2:
        print(seat - 1)
        break
    last_seat = seat
