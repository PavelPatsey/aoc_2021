with open('input example', 'r') as file:
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
    
    population[0] = population[1]
    population[1] = population[2]
    population[2] = population[3]
    population[3] = population[4]
    population[4] = population[5]
    population[5] = population[6]
    population[6] = population[7]
    population[7] = population[8]

    population[8] = n
    population[6] += n

    print('After',i,'days:',population)

population_size  = 0
for i in range(len(population)):
    population_size += population[i]

print('population_size = ',population_size)
