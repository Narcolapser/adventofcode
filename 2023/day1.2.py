lines = open('day1.input').read().split('\n')
#lines = open('day1.2.input').read().split('\n')

nums = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
        }

def starts_a(val):
    return any([key.startswith(val) for key in nums.keys()])

def is_a(val):
    return val in nums

def descend(current,rest):
    if is_a(current):
        return nums[current]
    elif starts_a(current):
        if len(rest):
            current += rest[0]
            rest = rest[1:]
            return descend(current,rest)
        else:
            return False
    else:
        return False

values = []
for line in lines:
    if len(line) == 0:
        continue
    stack = ''
    numbers = []
    pointer = 0
    while pointer < len(line):
        c = line[pointer]
        result = descend(c,line[pointer+1:])
        if result:
            numbers.append(result)
        pointer += 1
        
    first = numbers[0]
    last = numbers[-1]
    values.append(int(f'{first}{last}'))

print(values)
print(sum(values))
