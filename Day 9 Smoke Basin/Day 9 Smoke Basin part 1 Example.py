with open('input example', 'r') as file:
	data = file.read()

data = data.strip().split('\n')

string = ''
for i in range(len(data[0]) + 2):
    string += '9'

data = ['9' + x + '9' for x in data]
data = [string] + data + [string]

data = [[int(y) for y in x] for x in data]

Imax = len(data) - 1
Jmax = len(data[0]) - 1

# search minimals in modified table
mins = []
for i in range(Imax):
    for j in range(Jmax):
        if (data[i][j] < data[i][j - 1] and
            data[i][j] < data[i][j + 1] and
            data[i][j] < data[i + 1][j] and
            data[i][j] < data[i - 1][j]):
            mins.append(data[i][j])
print(mins)

answer = 0
for x in mins:
    answer += x + 1

print('answer =',answer)

# answer = 15
