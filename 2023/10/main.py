import random

def NeighborFetcher(maze,pos):
    x = pos[0]
    y = pos[1]
    result = {}
    if y != 0:
        result['u'] = maze[y-1][x]

    if x < len(maze[y])-1:
        result['r'] = maze[y][x+1]

    if y < len(maze) -1:
        result['d'] = maze[y+1][x]

    if x != 0:
        result['l'] = maze[y][x-1]
    
    return result

def PathFinder(neighbors,myself):
    result = set()
    if 'r' in neighbors:
        if neighbors['r'] in ['-','7','J','S']:
            result.add('r')
    
    if 'd' in neighbors:
        if neighbors['d'] in ['|','L','J','S']:
            result.add('d')
    
    if 'u' in neighbors:
        if neighbors['u'] in ['|','7','F','S']:
            result.add('u')
    
    if 'l' in neighbors:
        if neighbors['l'] in ['-','L','F','S']:
            result.add('l')

    my_dirs = set()
    if myself in ['-','L','F','S']:
        my_dirs.add('r')

    if myself in ['|','7','F','S']:
        my_dirs.add('d')

    if myself in ['|','L','J','S']:
        my_dirs.add('u')

    if myself in ['-','7','J','S']:
        my_dirs.add('l')

    return result.intersection(my_dirs)

def DirToPos(pos,dir):
    if dir == 'r':
        return (pos[0]+1,pos[1])
    if dir == 'l':
        return (pos[0]-1,pos[1])
    if dir == 'd':
        return (pos[0],pos[1]+1)
    if dir == 'u':
        return (pos[0],pos[1]-1)

def ForwardFinder(options, previous):
    previous_map = {'r':'l','l':'r','u':'d','d':'u'}
    #print(f'I came from {previous} and I have the current options: {options}')
    if len(options) != 2:
        print('It is broken!')
    for key in previous_map:
        if previous == key:
            return [i for i in options if i != previous_map[key]][0]

if __name__ == '__main__':
    #maze = open('sample1').read().split('\n')
    #maze = open('sample2').read().split('\n')
    maze = open('10/input').read().split('\n')
    start = None
    for y,line in enumerate(maze):
        for x,char in enumerate(line):
            if char == 'S':
                start = (x,y)
                break
        if start:
            break
    
    starting_dirs = PathFinder(NeighborFetcher(maze,start),maze[start[0]][start[1]])
    cur_dir = random.choice(list(starting_dirs))
    #cur_dir = 'r'
    cur_pos = DirToPos(start,cur_dir)
    next_pos = cur_pos
    steps = 1
    print(f'Moving {cur_dir} to {next_pos}. I have taken {steps} steps.')
    while next_pos != start:
        new_neighbors = NeighborFetcher(maze, cur_pos)
        next_dirs = PathFinder(new_neighbors,maze[cur_pos[1]][cur_pos[0]])
        #print(f'me {maze[cur_pos[1]][cur_pos[0]]} my neighbors {new_neighbors} my next paths {next_dirs} ')
        next_dir = ForwardFinder(next_dirs,cur_dir)
        next_pos = DirToPos(cur_pos,next_dir)

        cur_pos = next_pos
        cur_dir = next_dir
        steps += 1
        print(f'Moving {next_dir} to {next_pos}. I have taken {steps} steps.\n')
    print(f'Furthest point would be {steps/2}')