# функция поиска самой частовстреающейся цифры
# name(позиция где просматривать цифру, список)
# возвращает цифру 0 или 1
def the_most_frequent_number(position, list):

    N = len(list)
    
    # считаем кол-во '1' на позиции n
    sum = 0
    string = ''
    for i in range(N):
        string = list[i]
        sum += int(string[position])

    if sum >= N - sum:
        return 1
    else:
        return 0

# функция создает список с самой встречающейся цифрой на нужной позиции
# из исходного списка
# name(цифра, позиция где просматривать цифру, список)
# возвращает список
def the_most_frequent_number_list(number, position, list):

    N = len(list)

    new_list = []
    string = ''
    for i in range(N):
        string = list[i]
        if string[position] == str(number):
            new_list.append(string)

    return new_list


f = open("input.txt")

data = []
for line in f:
    data.append(line)

N = len(data)
M = len(data[0]) - 1


# o2
position = 0
o2 = data
while not (position > M or len(o2) == 1):
    number = the_most_frequent_number(position, o2)
    o2 = the_most_frequent_number_list(number, position, o2)
    position += 1
print('o2')
print(o2)


#co2
position = 0
co2 = data
while not (position > M or len(co2) == 1):
    number = the_most_frequent_number(position, co2)
    number = (number + 1) % 2
    co2 = the_most_frequent_number_list(number, position, co2)
    position += 1
print('co2')
print(co2)

o2_int = int(o2[0],2)
print('o2 =',o2_int)
co2_int = int(co2[0],2)
print('co2 =',co2_int)


answer = o2_int * co2_int
print('answer =',answer)

#answer = 1032597






