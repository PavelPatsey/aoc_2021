b = []
a = [[1, 2, 3], [4, 5, 6]]
b.append(a)
a = [[2, 1, 5], [0, 3, 7]]
b.append(a)

'''
for i in range(len(b)):
    for j in range(len(b[0])):
        print('\n')
        for k in range(len(b[0][0])):
            print(b[i][j][k])
print('2 part')
'''

'''
c = [0,1,2,3,4]
d = [1,3]
d = set(d)
print(d)
for i in range(len(c)):
    if i in d:
        print(i)
'''

'''
c = set() 
c.add(1)
c.add(1)
c.add(2)
'''

c = [0,1,2,3,4]
d = [1,3]
d = set(d)
print(d)
for i in range(len(c)):
    if i in d:
        print(i)



''''
for i in range(len(b)):
    for j in range(len(b[0])):
        print('\n')
        for k in range(len(b[0][0])):
            print(b[i][j][k])
'''
