# читаем данные из файла числа в список целых
with open("input.txt") as f:
    data = f.read().strip().split('\n')
    data = [int(x) for x in data]

N = len(data)

c = 0
for i in range(1, N):
    if data[i] > data[i - 1]:
        c = c + 1

print('c = ',c)



