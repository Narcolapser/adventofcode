lines = open('sample').read().split('\n')

stack = []
results = []
max_heat = 1000000

class Frame():
    city = None
    visited = None
    position = None
    last_3 = None
    heat_loss = None

def get_position(city, position, direction):
    if direction == 'u':
        if position[1] == 0:
            return False
        else:
            return (position[0],position[1]-1)
    
    if direction == 'd':
        if position[1] == len(city)-1:
            return False
        else:
            return (position[0],position[1]+1)
    
    if direction == 'l':
        if position[0] == 0:
            return False
        else:
            return (position[0]-1,position[1])
    
    if direction == 'r':
        if position[0] == len(city[0])-1:
            return False
        else:
            return (position[0]+1,position[1])

def check_final_pos(city, position):
    return position[1] == len(city) and position[0] == len(city[0])

def get_heat(city, position):
    return city[position[1]][position[0]]

def descend(frame):
    # Check if we are at the final destination
    if check_final_pos(frame.city, frame.position):
        results.append(frame.heat_loss+get_heat(frame.city, frame.position))
        return
    
    # Infinity protector
    if frame.heat_loss > max_heat:
        return

    # Find our possible directions
    directions = {'u','l','r','d'}

    # Remove edges
    directions = {d for d in directions if get_position(frame.city, frame.position, d)}

    # Check for 3 in a row
    last_set = set(frame.last_3)
    if len(last_set) == 1:
        directions = directions.difference(last_set)
    
    # Remove any direction that is a place we have previously visited.
    directions = {d for d in directions if get_position(frame.city, frame.position, d) not in frame.visited}

    # Now that we have reduced the possible locations, lets create new frames to throw on the stack of the remaining directions.
    for d in directions:
        f = Frame()
        f.city = frame.city
        f.visited = frame.visited.union({frame.position})
        f.position = get_position(frame.city, frame.position, d)
        f.last_3 = [i for i in frame.last_3]
        f.last_3.insert(0,d)
        while len(f.last_3) > 3:
            f.last_3.pop()
        f.heat_loss = frame.heat_loss + int(get_heat(frame.city, frame.position))
        stack.append(f)

if __name__ == '__main__':
    raw = open('sample').read()
    max_heat = sum([int(i) for i in raw if i.isdigit()])
    print(f'Max heat for this map: {max_heat}')
    first_frame = Frame()
    first_frame.city = raw.split('\n')
    first_frame.visited = set()
    first_frame.position = (0,0)
    first_frame.last_3 = []
    first_frame.heat_loss = 0
    stack.append(first_frame)
    while len(stack):
        frame = stack.pop()
        descend(frame)
        print(f'Frames left: {len(stack)} current highest heat: {max([frame.heat_loss for frame in stack])}                        ', end='\r')
    print()
    print(f'Shortest path: {min(results)}')
    print(f'Num of paths: {len(results)}')