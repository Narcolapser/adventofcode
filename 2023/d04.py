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

print(f'answer 1: pile_sum')

# Answer 2
cards = {}
for i,line in enumerate(lines):
    winners, numbers = line.split(':')[1].split('|')
    winners = {int(i) for i in winners.split(' ') if i.isdigit()}
    numbers = {int(i) for i in numbers.split(' ') if i.isdigit()}
    matches = len(numbers.intersection(winners))
    cards[i] = {'matches':matches,'worth': 2**(matches-1) if matches else 0}

pile_sum = 0
# Now recurse through the deck finding value
def copies_value(pos):
    if pos >= len(cards) - 1:
        return 0
    value = 1
    for i in range(cards[pos]['matches']):
        value += copies_value(pos+i+1)
    return value

for c, card in enumerate(cards):
    pile_sum += 1
    for i in range(cards[card]['matches']):
        pile_sum += copies_value(c+i+1)

print(pile_sum)