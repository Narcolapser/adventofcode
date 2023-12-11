#lines = open('d08.sample').read().split('\n')
#lines = open('d08.sample2').read().split('\n')
lines = open('d08.input').read().split('\n')

def link_to_bits(line):
    parts = line.split(' = ')
    left, right = parts[1].replace('(','').replace(')','').replace(',','').split(' ')
    return [parts[0],left, right]

path = lines[0]
#start = lines[2].split(' ')[0]
start = 'AAA'
parsed_links = [link_to_bits(link) for link in lines[2:]]

links = {link[0]:{'L':link[1],'R':link[2]} for link in parsed_links}

position = start
count = 0
while position != 'ZZZ':
    path_position = count%len(path)
    print(f'Current position in path is {path_position} with a value of {path[path_position]}')
    position = links[position][path[path_position]]
    count += 1

print(f'steps taken: {count}')
