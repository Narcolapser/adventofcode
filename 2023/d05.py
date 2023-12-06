# Sort the lines.
# Start with an empty array. 

segments = open('d05.sample').read().split('\n\n')

seeds = [int(i) for i in segments[0].split(':')[1].split(' ') if i.isdigit()]

for segment in segments[1:]:
    raw_lines = segment.split('\n')
    lines = []
    for line in raw_lines[1:]:
        lines.append([int(i) for i in line.split(' ') if i.isdigit()])
    lines.sort()
    
    # Now that we have the lines sorted, lets build out the mappings.
    operating_line = lines.pop(0)
    i = 0
    stash = []
    mapping = {}
    while True:
        if i < operating_line[0]:
            if len(stash):
                mapping[i] = stash.pop(0)
            else:
                mapping[i] = i
            i += 1
        else:
            for j in range(operating_line[2]):
                mapping[i] = operating_line[1]+j
                i += 1

            if len(lines) == 0:
                break
            else:
                operating_line = lines.pop(0)
    
    while len(stash):
        mapping[i] = stash.pop(0)
    print(mapping)