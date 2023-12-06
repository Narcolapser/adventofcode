# lets break this up logically. Let's make range objects.
# Given a value, can you identify whether that value is inside your range?
# If it is inside your range, what does it map to? 
# If none of the range objects identify with the value, then we know it is a straight pass through.

#segments = open('d05.sample').read().split('\n\n')
segments = open('d05.input').read().split('\n\n')

#seeds = [int(i) for i in segments[0].split(':')[1].split(' ') if i.isdigit()]
seed_digits = [int(i) for i in segments[0].split(':')[1].split(' ') if i.isdigit()]
seeds = []
while len(seed_digits):
    start = seed_digits.pop(0)
    seed_range = seed_digits.pop(0)
    for i in range(seed_range):
        seeds.append(start+i)

print(len(seeds))
class Range():
    def __init__(self,range_line):
        self.destination, self.source, self.range = [int(i) for i in range_line.split(' ') if i.isdigit()]

    def __contains__(self,value):
        if value < self.source:
            return False
        elif value > self.source + self.range - 1:
            return False
        else:
            return True

    def map(self,value):
        if value not in self:
            return False
        return self.destination + (value - self.source )

class RangeMap():
    def __init__(self, ranges):
        self.ranges = ranges
    
    def map(self,value):
        for range in self.ranges:
            if value in range:
                return range.map(value)
        return value

maps = []
for segment in segments[1:]:
    ranges = [Range(line) for line in segment.split('\n')[1:] if ' ' in line]
    maps.append(RangeMap(ranges))

locations = []

for seed in seeds:
    value = seed
    for rmap in maps:
        value = rmap.map(value)
    locations.append(value)

print(min(locations))
