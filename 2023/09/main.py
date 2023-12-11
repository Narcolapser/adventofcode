class Row():
    def __init__(self,row):
        self.values = [int(i) for i in row.split(' ') if i.isdigit()]
    
    def predict(self,value):
        if sum(self.values) == 0:
            return 0
        else:
            return self.values[-1] + value
    
    def __eq__(self, other):
        if len(self.values) != len(other.values):
            return False
        
        for i,value in enumerate(self.values):
            if value != other.values[i]:
                return False
        
        return True

    def get_descendant(self):
        if sum(self.values) == 0:
            return False
        
        if len(self.values) == 1:
            return Row('0')
        
        previous = self.values[0]
        new_values = []
        for i in self.values[1:]:
            new_values.append(str(i - previous))
            previous = i

        return Row(' '.join(new_values))

    def expand(self):
        if sum(self.values) == 0:
            self.values.append(0)
            return 0

        descendant = self.get_descendant()
        descendant.expand()
        next_value = self.predict(descendant.values[-1])
        self.values.append(next_value)
        return next_value
    
    def __str__(self):
        return ' '.join([str(val) for val in self.values])
    
    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    #lines = open('sample').read().split('\n')
    lines = open('input').read().split('\n')
    rows = [Row(line) for line in lines]
    print(f'Number of rows: {len(rows)}')
    increment = 0
    for i,row in enumerate(rows):
        next_value = row.expand()
        print(f'row: {i} extrapolated value of {next_value}')
        increment += next_value
    
    print(f'historic increment: {increment}')
