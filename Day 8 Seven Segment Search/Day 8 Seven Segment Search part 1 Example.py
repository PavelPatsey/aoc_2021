with open('input example', 'r') as file:
	data = file.read()

data = data.strip().split('\n')
data = [x.strip().split('|') for x in data]

signal_patterns = [x[0].strip() for x in data]
output_values = [x[1].strip() for x in data]

signal_patterns = [x.split() for x in signal_patterns]
output_values = [x.split() for x in output_values]

counter = 0
for x in output_values:
    for y in x:
        if len(y) in {2, 4, 3, 7}:
            counter += 1

print('counter =',counter)

