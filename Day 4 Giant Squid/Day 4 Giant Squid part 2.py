def sum_of_all_unmarked_numbers(number_of_grid,marks, board):

    sum = 0
    i = number_of_grid
    for j in range(5):
        for k in range(5):
            if marks[i][j][k] == 0:
                sum += board[i][j][k]
                #print(i,j,k,board[i][j][k])
    return sum
    

def bingo(list):
    #list[][]
    #return true o false

    answer = False

    sum = 0
    # run strings
    for j in range(5):
        for k in range(5):
            sum += list[j][k]
        if sum == 5:
            answer = True
        sum = 0
    
    # run columns
    sum = 0
    for j in range(5):
        for k in range(5):
            sum += list[k][j]
        if sum == 5:
            answer = True
        sum = 0

    return answer

def mark_list(n, board, marks):
    # n int
    # board[][][]
    # marks[][][]

    for i in range(len(board)):
        for j in range(5):
            for k in range(5):
                if n == board[i][k][j]:
                    marks[i][k][j] = 1



with open('input', 'r') as file:
	data_str = file.read()

# one string
data_str = data_str.strip()
# list of 2 strings: numbers and tables
data = data_str.split('\n',1)

# first line
numbers_str = data[0]
# list of strings
numbers = numbers_str.split(',')
# list of int for the first line
numbers = [int(x) for x in numbers]


data[1] = data[1].strip()

# creat list of 2d lists - to store information about tables
# board_str[] = list of grids_str
# grid[][] = list of numbers
# grid[][][] = 3d list of numbers

# create list of strings
board_strs = data[1].split('\n\n')
# create list of list of strings
grid_strs = [x.split('\n') for x in board_strs]


# grid[][][] = 3d list of numbers
board = []
for i in range(len(grid_strs)):
    grid1 = [x.strip().split() for x in grid_strs[i]]
    grid1 = [[int(y) for y in x] for x in grid1]
    board.append(grid1)


# creat list of marks with nulls
marks = []
for i in range(len(board)):
    marks.append([])
for i in range(len(board)):
    for j in range(5):
        marks[i].append([])
for i in range(len(board)):
    for j in range(5):
        for k in range(5):
            marks[i][j].append(0)
    
# start solve the task

set_of_winner_grids = set()
while not len(set_of_winner_grids) == len(marks):
    for j in range(len(marks)):
        if not j in set_of_winner_grids:
            i = -1
            while not bingo(marks[j]) == True:
                i += 1
                #print(numbers[i])
                mark_list(numbers[i], board, marks)
                #print(bingo(marks[j]))
                last_number = numbers[i]
                s = sum_of_all_unmarked_numbers(j, marks, board)
            set_of_winner_grids.add(j)

number_of_grid = j
print('number_of_grid = ', number_of_grid)
print('last_number =', last_number)
print('s = ',s)
answer = s * last_number
print('answer =',answer)

'''
number_of_grid =  99
last_number = 73
s =  116
answer = 8468
'''



        

