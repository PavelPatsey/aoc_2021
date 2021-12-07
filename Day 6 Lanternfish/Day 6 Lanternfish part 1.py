with open('input', 'r') as file:
	data = file.read()

number_of_days = 80 # !!! 18 or 80

data = data.strip().split(',')
data = [int(x) for x in data]

population = []
population = [x for x in data]

print('Initial state:',population)

for day in range(1, number_of_days + 1):
    i = 0
    counter = 0
    while not i > len(population) - 1:
        if population[i] > 0:
            population[i] -= 1
        else:
            population[i] = 6
            counter += 1
        i += 1
    for _ in range(counter):
        population.append(8)
    print('After',day,'day:')

answer = len(population)

print('answer =', answer)




