f = open("input Example.txt")

data = []
for line in f:
    data.append(line)
    print(line)

N = len(data)
print('N = ',N)

import re

horizontal_position = 0
depth = 0
for i in range(N):
    token = re.split(" |\n", data[i])
    print(i, token[0], int(token[1]))
    if token[0] == 'forward':
        horizontal_position += int(token[1])
    elif token[0] == 'down':
        depth += int(token[1])
    elif token[0] == 'up':
        depth -= int(token[1])
    else:
        print('Error!')


print('answer =',horizontal_position * depth)


#13 * 21 = 273


    
