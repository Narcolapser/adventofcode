def roll_row_north(current, northern):
    if northern is None:
        return (current, northern)
    
    new_northern = ''
    new_current = ''
    for i,slot in enumerate(current):
        if slot == 'O' and northern[i] == '.':
            new_northern += 'O'
            new_current += '.'
        else:
            new_current += slot
            new_northern += northern[i]
    
    return (new_current, new_northern)

def weigh_row(row, position):
    rocks = len([rock for rock in row if rock == 'O'])
    return rocks * position

if __name__ == '__main__':
    lines = open('input').read().split('\n')
    itterations = len(lines)
    while itterations > 0:
        for i in range(itterations)[1:]:
            northern = lines[i-1]
            current = lines[i]
            current, northern = roll_row_north(current, northern)
            lines[i-1] = northern
            lines[i] = current
        itterations -= 1
    
    for line in lines:
        print(line)
    
    weight = sum([weigh_row(row,len(lines)-i) for i,row in enumerate(lines)])
    print(weight)