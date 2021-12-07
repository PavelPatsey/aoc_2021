f = open("input.txt")

data = []
for line in f:
    data.append(line)

N = len(data)

import re

horizontal_position = 0
depth = 0
aim = 0
for i in range(N):
    token = re.split(" |\n", data[i])
    if token[0] == 'forward':
        horizontal_position += int(token[1])
        depth += aim * int(token[1])
    elif token[0] == 'down':
        aim += int(token[1])
    elif token[0] == 'up':
        aim -= int(token[1])
    else:
        print('Error!')


print('answer =',horizontal_position * depth)

# answer = 1459206


    
