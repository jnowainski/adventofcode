import os
import re

stream = open(os.path.dirname(os.path.abspath(__file__))+'/data.txt')

data = stream.read().split('\n')

for d in data:
    if 'shiny gold bag' in d:
        print(d)