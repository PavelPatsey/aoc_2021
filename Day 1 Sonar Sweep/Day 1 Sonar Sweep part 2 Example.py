'''
with open("input.txt") as f:
    data = f.read().strip().split('\n')
    data = [int(x) for x in data]

N = len(data)

c = 0
for i in range(1, N):
    if data[i] > data[i - 1]:
        c = c + 1

print('c = ',c)
'''

'''
data = [
173,
179,
200,
210,
226,
229,
220,
221,
228,
233,
237,
238,
249,
261,
284,
285,
287,
289
]

N = len(data)

s1 = 0
s2 = 0
c = 0
for i in range (3, N):
    s1 = data[i -1] + data[i - 2] + data[i - 3]
    s2 = data[i] + data[i - 1] + data[i - 2]
    if s2 > s1:
        c = c + 1

print('c = ',c)
    

# anwer 13
'''

# читаем данные из файла числа в список целых
with open("input.txt") as f:
    data = f.read().strip().split('\n')
    data = [int(x) for x in data]

N = len(data)

s1 = 0
s2 = 0
c = 0
for i in range (3, N):
    s1 = data[i -1] + data[i - 2] + data[i - 3]
    s2 = data[i] + data[i - 1] + data[i - 2]
    if s2 > s1:
        c = c + 1

print('c = ',c)

