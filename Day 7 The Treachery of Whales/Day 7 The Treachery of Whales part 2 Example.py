def fuel_cost(n):
    
    return int(n * (n+1) / 2)
        

with open('input example', 'r') as file:
	data = file.read()

data = data.strip().split(',')
data = [int(x) for x in data]

max_data = 0
for x in data:
    if x > max_data:
        max_data = x

min_cost_fuel = 0
for x in data:
    min_cost_fuel += fuel_cost(x)
for i in range(max_data + 1):
    summ = 0
    for x in data:
        summ += fuel_cost(abs(x - i))
    if summ < min_cost_fuel:
        min_cost_fuel = summ

print('min_cost_fuel =',min_cost_fuel)




