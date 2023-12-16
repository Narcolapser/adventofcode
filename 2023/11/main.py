def check_row(row):
    return '#' in row

def pivot(galaxy):
    rows = [[] for i in galaxy[0]]
    for i in range(len(galaxy)):
        for n,row in enumerate(rows):
            row.append(galaxy[i][n])
    result = [''.join(row) for row in rows]
    return result

def find_pairs(galaxy):
    spots = []
    for i,row in enumerate(galaxy):
        for j,c in enumerate(row):
            if c == '#':
                spots.append((i,j))
    
    pairs = []
    for i,s1 in enumerate(spots):
        for j,s2 in enumerate(spots[i+1:]):
            pairs.append((s1,s2))
    
    return pairs

def expand_galaxy(galaxy):
    new_galaxy = []
    for row in galaxy:
        if not check_row(row):
            new_galaxy.append(row)
        new_galaxy.append(row)
    
    pivoted = pivot(new_galaxy)
    final = []
    for row in pivoted:
        if not check_row(row):
            final.append(row)
        final.append(row)

    return pivot(final)

def find_distance(s1, s2):
    x = abs(s1[0]-s2[0])
    y = abs(s1[1]-s2[1])
    # We can just add the values if they are in a straight line, but diagonals are less 1.
    distance = x+y
    distance -= 0 if x==0 or y==0 else 1
    return distance

if __name__ == '__main__':
    galaxy = open('sample').read().split('\n')
    
    # expand it
    expanded = expand_galaxy(galaxy)

    # find the pairs
    pairs = find_pairs(expanded)

    # find the distances
    distances = [find_distance(*pair) for pair in pairs]

    # sum and print
    print(sum(distances))