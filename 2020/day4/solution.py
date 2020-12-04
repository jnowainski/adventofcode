import os
import re
stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n\n')

# requirement list
rl = [
    'byr', # (Birth Year)
    'iyr', # (Issue Year)
    'eyr', # (Expiration Year)
    'hgt', # (Height)
    'hcl', # (Hair Color)
    'ecl', # (Eye Color)
    'pid', # (Passport ID)
    #'cid' # (Country ID), optional
]

# part 1
valid_counter = 0

for passport in data:
    if all([r in passport for r in rl]):
        valid_counter += 1

print('PART 1: ',valid_counter)

# part 2

'''

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''
def check_field(field, val):
    if field == 'byr':
        if len(val)!= 4 or int(val)<1920 or int(val)>2002:
            return False

    if field == 'iyr':
        if len(val)!=4 or int(val)<2010 or int(val)>2020:
            return False

    if field == 'eyr':
        if len(val)!=4 or int(val)<2020 or int(val)>2030:
            return False
        
    if field == 'hgt':
        if 'cm' in val:
            t_val = val.split('cm')[0]
            if (int(t_val)<150 or int(t_val)>193):
                return False
        elif 'in' in val:
            t_val = val.split('in')[0]
            if (int(t_val)< 59 or int(t_val)> 76):
                return False
        else:
            return False

    if field == 'hcl':
        if re.match(re_hcl, val)==None or not val == re.match(re_hcl, val).string:
            return False

    if field == 'ecl':
        if not any([ecl in val for ecl in ecl_list]) or len(val)!=3:
            return False
    if field == 'pid':
        if re.fullmatch(re_pid, val)==None or not val == re.fullmatch(re_pid, val).string:
            return False
    return True


re_hcl = '(#([a-f0-9]{6}))'
re_pid = '([0-9]{9})'
ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid_counter = 0

first_valid = []
for passport in data:
    if all([r in passport for r in rl]):
        first_valid.append(passport)

for valid_passport in first_valid:
    # generate dict
    fields = re.split(r' |\n', valid_passport)
    flag = 0

    for f in fields:
        field = f.split(':')[0]
        val = f.split(':')[1]
        if not check_field(field, val):
            flag = 1
    
    if flag == 0:
        valid_counter+= 1
        #print('VALID PASSPORT: ',valid_passport+'\n')

print('PART 2: ', valid_counter)


