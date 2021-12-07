f = open("input example.txt")

data = []
for line in f:
    data.append(line)

N = len(data)
M = 5

s = []
for i in range(M):
    s.append(0)
 
for i in range(N):
    string = data[i]
    for j in range(M):
        s[j] += int(string[j])

gamma = ''
epsilon = ''
for i in range(M):
    if s[i] > N / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma)
print(epsilon)

gamma_int = int(gamma,2)
epsilon_int = int(epsilon,2)

print(gamma_int)
print(epsilon_int)

answer = gamma_int * epsilon_int

print('answer =',answer)


"""
gamma = '10110'
gamma = int(gamma,2)
print(gamma)
"""
'''
gamma = 10110
gamma = str(gamma)
gamma = int(gamma,2)
print(gamma)
'''
