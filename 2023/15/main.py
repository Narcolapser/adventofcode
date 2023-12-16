def hash_string(string):
    result = 0
    for c in string:
        result += ord(c)
        result *= 17
        result %= 256
    return result

def hash_line(line):
    return sum([hash_string(i) for i in line.split(',')])

if __name__ == '__main__':
    line = open('input').read().split('\n')[0]
    print(hash_line(line))
