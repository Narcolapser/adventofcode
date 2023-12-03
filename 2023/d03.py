lines = open('03.sample').read().split('\n')
lines = open('d03.input').read().split('\n')

# I could attempt to make a multi dimensional linked list so each symbol points to it's associated numbers.
# This would mean I just request all the symbols and then request all the numbers they are next too. 

# Alternatively. I could search each row for symbols and then identify numbers in the surrounding 8 spaces.
# For this I would either need to setup a system for identifying the numbers that grow off of the neighbooring spaces
# or I would have to replace the numbers and avoid adding the same number twice by mistake.

# I think I'll go for the last option.

def line_seek(line,pos):
    # Search left
    left = ''
    left_cursor = pos -1
    while left_cursor >= 0 and line[left_cursor].isdigit():
        left = line[left_cursor] + left
        left_cursor-=1

    mid = line[pos] if line[pos].isdigit() else ''

    # search right
    right = ''
    right_cursor = pos + 1
    while right_cursor < len(line) and line[right_cursor].isdigit():
        right += line[right_cursor]
        right_cursor +=1
    
    # If mid is a number, then we must concat everything.
    if mid.isdigit():
        return [int(left+mid+right)]
    
    # If not, then we have at most two digits.
    result = []
    if left.isdigit():
        result.append(int(left))
    
    if right.isdigit():
        result.append(int(right))
    
    return result

# part_sum = 0
# for i,line in enumerate(lines):
#     cursor = 0
#     while cursor < len(line):
#         if line[cursor] not in ['0','1','2','3','4','5','6','7','8','9','.']:
#             # We have found a symbol. Now let us look for the numbers around it.
#             # Are we at the top? If not we need to search above.
#             if i > 0:
#                 part_sum += sum(line_seek(lines[i-1],cursor))
            
#             # check for numbers either side of the current position.
#             part_sum += sum(line_seek(line,cursor))

#             # Check below, unless we are at the bottom.
#             if i < len(lines):
#                 part_sum += sum(line_seek(lines[i+1],cursor))
#         cursor += 1
           
# print(part_sum)

# Answer part 2
ratio_sum = 0
for i,line in enumerate(lines):
    cursor = 0
    while cursor < len(line):
        if line[cursor] == '*':
            # We have found a symbol. Now let us look for the numbers around it.
            # Are we at the top? If not we need to search above.
            gear_list = []
            if i > 0:
                gear_list += line_seek(lines[i-1],cursor)
            
            # check for numbers either side of the current position.
            gear_list += line_seek(line,cursor)

            # Check below, unless we are at the bottom.
            if i < len(lines):
                gear_list += line_seek(lines[i+1],cursor)
            
            # We only care if there are exactly two part numbers
            if len(gear_list) == 2:
                ratio_sum += gear_list[0] * gear_list[1]
        cursor += 1
print(ratio_sum)