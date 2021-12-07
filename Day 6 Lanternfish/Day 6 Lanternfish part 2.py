with open('input', 'r') as file:
	data = file.read()

number_of_days = 256 # !!! 18 or 80 or 256

data = data.strip().split(',')
data = [int(x) for x in data]

population = []
population = [0 for i in range(9)]

for x in data:
    population[x] += 1

for i in range(1, number_of_days + 1):
    n = population[0]

    for j in range(len(population) - 1):
        population[j] = population[j + 1]
       
    population[8] = n
    population[6] += n

    print('After',i,'days:',population)

population_size  = 0
for x in population:
    population_size += x

print('population_size = ',population_size)

# population_size =  1765974267455
