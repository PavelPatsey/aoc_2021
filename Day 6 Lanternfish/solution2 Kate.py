from collections import Counter

with open('input.in', 'r') as file:
	fishes = file.read().split(',')

# идея в том, чтобы считать увеличение количества рыб на каждый день
# например здесь мы получаем список {3: 2, 4: 1, 1: 1, 2: 1}
# то есть третьего числа количество рыб увеличится на два
fishes = Counter([int(fish) for fish in fishes])

def population(fishes, n):
	initial = fishes.copy()
	summ = sum(initial.values())

	for day in range(n):
		# каждый день проверяем, на сколько увеличилось количество рыб
		today_number = initial[day]
		summ += today_number
		# каждая новая рыба означает, что через шесть дней рыба-мать создаст ещё одну рыбу
		initial[day + 7] += today_number
		# и что эта новая рыба через 8 дней сама станет рыбой-матерью
		initial[day + 9] += today_number

	return summ

print(population(fishes, 80))
print(population(fishes, 256))
