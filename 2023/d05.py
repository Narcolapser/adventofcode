MAX_INT = 10**40 # Python has no max int. I just need an absurdly large number.

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

    def map_extended(self,value):
        if value not in self:
            return False
        mapping = self.destination + (value - self.source )
        left = self.range - (value - self.source) -1
        return {'map':mapping, 'more':left}

class RangeMap():
    def __init__(self, name, ranges, next_range):
        self.name = name
        self.ranges = ranges
        self.low_points = {r.source:r for r in ranges}
        self.next_range = next_range
    
    def map(self,value):
        for range in self.ranges:
            if value in range:
                return range.map(value)
        return value
    
    def map_range(self,value):
        for range in self.ranges:
            if value in range:
                return range.map_extended(value)
        # If we are here none of our ranges match. But we need to find the when the next range will pickup.
        finders = [r.source-value for r in self.ranges if r.source-value > 0]
        more = min(finders) if len(finders) else MAX_INT
        return {'map':value, 'more':more}
    
    def map_extended(self,value):
        ''' given value, what does it map to and how long will it stay that way?'''
        result = self.map_range(value)
        value = result['map']
        more = result['more']
        if self.next_range:
            lower = self.next_range.map_extended(value)
            value = lower['map']
            more = min([lower['more'],more])
        return {'map':value, 'more':more}

if __name__ == '__main__':
    #segments = open('d05.sample').read().split('\n\n')
    segments = open('d05.input').read().split('\n\n')

    #seeds = [int(i) for i in segments[0].split(':')[1].split(' ') if i.isdigit()]
    seed_digits = [int(i) for i in segments[0].split(':')[1].split(' ') if i.isdigit()]
    seed_ranges = []
    while len(seed_digits):
        start = seed_digits.pop(0)
        seed_range = seed_digits.pop(0)
        seed_ranges.append((start,seed_range))

    maps = []
    for segment in segments[1:]:
        ranges = [Range(line) for line in segment.split('\n')[1:] if ' ' in line]
        maps.append(RangeMap(ranges))

    # given a seed range start from it's lowest point, map that.
    # Now find the start of the first range. Skip every number between the lowest and the start
    # Find that range's lowest point and map that. Skip the remaining mappings.
    # Map the start of the next un-mapped range to the bottom of the next range.
    # Repeat this until we get to the end of the seed range.
