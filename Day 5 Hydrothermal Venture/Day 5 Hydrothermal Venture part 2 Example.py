with open('input example', 'r') as file:
	data = file.read()
import re
data = data.strip().replace('->',',')
data = data.strip().split('\n')
data = [x.split(',') for x in data]
data = [[int(x.strip()) for x in data[i]] for i in range(len(data))]


maxdata = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] > maxdata:
            maxdata = data[i][j] 

# creat points list and fill it with nulls
points = []
for i in range(maxdata + 1):
    points.append([])

for i in range(maxdata + 1):
    for j in range(maxdata + 1):
        points[i].append(0)


# fill pointlist with



for i in range(len(data)):
    x1 = data[i][0]
    y1 = data[i][1]
    x2 = data[i][2]
    y2 = data[i][3]

        
    # x1 == x2
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for j in range(y1, y2 + 1):
            points[j][x1] += 1
    # y1 == y2
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for j in range(x1, x2 + 1):
            points[y1][j] += 1
    elif  abs(x2 - x1) == abs(y2 - y1):
        dx = int((x2 - x1)/(abs(x2 - x1)))
        dy = int((y2 - y1)/(abs(y2 - y1)))
        i = 0
        while not i > abs(x2 - x1):
            points[y1 + i*dy][x1 + i*dx] += 1
            i += 1

    

for i in range(len(points)):
    print(points[i])
            


# count 2 in points list
counter = 0
for i in range(len(points)):
    for j in range(len(points)):
        if points[i][j] >= 2:
            counter += 1

print('counter =',counter)





