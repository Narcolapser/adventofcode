lines = open("d04.sample").read().split('\n')
lines = open("d04.input").read().split('\n')

pile_sum = 0
for line in lines:
    winners, numbers = line.split(':')[1].split('|')
    winners = {int(i) for i in winners.split(' ') if i.isdigit()}
    numbers = {int(i) for i in numbers.split(' ') if i.isdigit()}
    matches = len(numbers.intersection(winners))
    if matches:
        pile_sum += 2**(matches-1)

print(pile_sum)