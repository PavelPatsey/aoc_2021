def destroy_basin(basins):
    """basin - list[][]"""
    for i in range(len(basins) - 1):
        for j in range(len(basins[0]) - 1):
            if basins[i][j] == 1:
                basins[i][j] = 9                   

def size_of_basin(basin):
    """basin - list[][]"""
    counter = 0
    for x in basin:
        for y in x:
            if y == 1:
                counter += 1
    return counter

def find_basin(i, j, basins):
    """i and j are indexes of element
    basin - list[][]
    """
    basins[i][j] = 1
    
    for di, dj in [(1,0), (0, 1), (-1, 0), (0, -1)]:
        if basins[i + di][j + dj] != 9 and basins[i + di][j + dj] != 1:
            find_basin(i + di, j + dj, basins)
    
# start main program
with open('input example', 'r') as file:
	data = file.read()

data = data.strip().split('\n')

string = ''
for i in range(len(data[0]) + 2):
    string += '9'

# add 9 around the entire table
# in order not to look for the boundary conditions 
data = ['9' + x + '9' for x in data]
data = [string] + data + [string]

data = [[int(y) for y in x] for x in data]

Imax = len(data) - 1
Jmax = len(data[0]) - 1

# create basins list and fill it by 0 and 9
basins = []

basins = [[0 for j in range(Jmax + 1)] for i in range(Imax + 1)]

for i in range(Imax + 1):
    for j in range(Jmax + 1):
        if data[i][j] == 9:
            basins[i][j] = 9

# find the sizes of the basins 
basins_sizes = []
for i in range(Imax):
    for j in range(Jmax):
        if basins[i][j] != 9:
            find_basin(i, j, basins)
            basins_sizes.append(size_of_basin(basins))
            destroy_basin(basins)

# answer output  
print('basins_sizes =',basins_sizes)
basins_sizes.sort()
print('basins_sizes =',basins_sizes)

bs_max = len(basins_sizes) - 1

answer = basins_sizes[bs_max] * basins_sizes[bs_max - 1] * basins_sizes[bs_max - 2]
print('answer =',answer)
