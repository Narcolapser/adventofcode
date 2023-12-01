lines = open('day1.input').read().split('\n')

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

values = []
for line in lines:
    if len(line) == 0:
        continue
    stack = ''
    numbers = []
    for c in line:
        if is_a(c):
            numbers.append(nums[c])
            stack = ''
        else:
            stack += c
            if is_a(stack):
                numbers.append(nums[stack])
                stack = ''
            else:
                if starts_a(stack):
                    continue
                else:
                    stack = c
        
    first = numbers[0]
    last = numbers[-1]
    values.append(int(f'{first}{last}'))

print(values)
print(sum(values))
