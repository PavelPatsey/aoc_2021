with open('input example', 'r') as file:
	data = file.read()

data = data.strip().split(',')
data = [int(x) for x in data]

max_data = 0
for x in data:
    if x > max_data:
        max_data = x

fuel = []
for _ in range(max_data + 1):
    fuel.append(0)

for i in range(len(fuel)):
    for y in data:
        fuel[i] += abs(y - i)

min_cost_fuel = fuel[0]
for x in fuel:
    if x < min_cost_fuel:
        min_cost_fuel = x

print('min_cost_fuel =',min_cost_fuel)
