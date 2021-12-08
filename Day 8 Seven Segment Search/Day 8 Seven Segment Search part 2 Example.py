def decrypt_the_string(d, string):
    # d - словарь
    # string - строка

    decrypted_string = None
    for i in range(len(d)):
        if d[i] == set(string):
            decrypted_string = i

    return decrypted_string
    
def find_dictionary(signal_patterns):
    # тип signal_patterns = list
    # return d типа словарь

    number0 = set() # len = 6
    number1 = set() # len = 2 !
    number2 = set() # len = 5
    number3 = set() # len = 5
    number4 = set() # len = 4 !
    number5 = set() # len = 5
    number6 = set() # len = 6
    number7 = set() # len = 3 !
    number8 = set() # len = 7 !
    number9 = set() # len = 6
    number069 = set() # len = 6 !
    number235 = set() # len = 5 !

    # ищем сеты для чисел 1, 4, 7, 8 и чисел из {2, 3, 5} и из {0, 6, 9} 
    for y in signal_patterns:
            if len(y) == 2:
                number1 = set(y)
            elif len(y) == 4:
                number4 = set(y)
            elif len(y) == 3:
                number7 = set(y)
            elif len(y) == 7:
                number8 = set(y)
            elif len(y) == 5:
                number235 = number235.union(set(y))
            elif len(y) == 6:
                number069 = number069.union(set(y))
            else:
                print('Error in len(y)')
    '''
     aaaa
    b    c
    b    c
     dddd
    e    f
    e    f
     gggg
    '''

    cf = number1
    bcdf = number4
    acf = number7
    abcdefg = number8


    # abfg = inter069
    inter069 = set()
    number_found = False
    for y in signal_patterns:
            if len(y) == 6 and number_found  == False:
                inter069 = set(y)
                number_found = True
            if len(y)== 6 and number_found  == True:
                inter069 = inter069.intersection(set(y))
    abfg = inter069 # abfg = inter069
    cde = abcdefg - abfg # number8 - inter069 т.е. cde = abcdefg - abfg

    # adg = inter235
    inter235 = set()
    number_found = False
    for y in signal_patterns:
            if len(y) == 5 and number_found  == False:
                inter235 = set(y)
                number_found = True
            if len(y)== 5 and number_found  == True:
                inter235 = inter235.intersection(set(y))
    adg = inter235 # adg = inter235
    bcef = abcdefg - adg # number8 - inter2345 т.е. bcef = abcdefg - adg

    # f
    f = cf - cde
    # c
    c = cf - abfg
    # d
    bd = bcdf - cf
    d = bd - abfg
    # b
    b = bcdf - f - c - d
    # a
    a = acf - c - f
    # g
    g = adg - a - d
    # e
    e = bcef - b - c - f

    # словарь цифр
    d = dict([
        (0, a.union(b,c,e,f,g)), # abcefg
        (1, c.union(f)), # cf
        (2, a.union(c,d,e,g)), # acdeg
        (3, a.union(c,d,f,g)), # acdfg
        (4, b.union(c,d,f)), # bcdf
        (5, a.union(b,d,f,g)), # abdfg
        (6, a.union(b,d,e,f,g)), # abdefg
        (7, a.union(c,f)), # acf
        (8, a.union(b,c,d,e,f,g)), # abcdefg
        (9, a.union(b,c,d,f,g)), # abcdfg
        ]) 

    return d

# начало основной программы
with open('input example', 'r') as file:
	data = file.read()

data = data.strip().split('\n')
data = [x.strip().split('|') for x in data]

signal_patterns = [x[0].strip() for x in data]
output_values = [x[1].strip() for x in data]

signal_patterns = [x.split() for x in signal_patterns]
output_values = [x.split() for x in output_values]

answer = 0
for i in range(len(signal_patterns)):
    # найдем словарь цифр
    d = find_dictionary(signal_patterns[i])
    # находим зашифрованное число в первой строчке
    number = ''
    for x in output_values[i]:
        number += str(decrypt_the_string(d, x))
    number = int(number)
    answer += number
    print('i =',i,'number =', number)

print('answer =', answer)

# answer = 61229
