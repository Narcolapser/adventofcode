lines = open('02.sample').read().split('\n')
lines = open('02.input').read().split('\n')

games = {}
for line in lines:
    game_part, rounds = line.split(':')
    game = int(game_part.split(' ')[1])
    games[game] = {'red':0,'green':0,'blue':0}
    for round in rounds.split(';'):
        for tuple in round.split(','):
            num, color = tuple.strip().split(' ')
            num = int(num)
            games[game][color] = max(num,games[game][color])

compare_set = {'red':12,'green':13,'blue':14}

game_sum = 0
for game in games:
    possible = True
    for color in compare_set:
        if games[game][color] > compare_set[color]:
            possible = False
    
    if possible:
        game_sum += game

print(games)
print(game_sum)