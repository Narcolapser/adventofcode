lines = open('day1.input').read().split('\n')

values = []
for line in lines:
    if len(line) == 0:
        continue
    numbers = [i for i in line if i.isdigit()]
    first = numbers[0]
    last = numbers[-1]
    values.append(int(f'{first}{last}'))

print(values)
print(sum(values))
