class Row():
    def __init__(self,row):
        self.values = [int(i) for i in row.split(' ') if i.isdigit()]
        self.descendant = None
    
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
        if self.descendant:
            return self.descendant
        else:
            if sum(self.values) == 0:
                return False
            
            if len(self.values) == 1:
                return Row('0')
            
            previous = self.values[0]
            new_values = []
            for i in self.values[1:]:
                new_values.append(str(i - previous))
                previous = i

            self.descendant = Row(' '.join(new_values))
            return self.descendant
            

    def expand(self):
        if sum(self.values) == 0:
            self.values.append(0)
            return 0

        descendant = self.get_descendant()
        stack.append(descendant)
        descendant.expand()
        next_value = self.predict(descendant.values[-1])
        self.values.append(next_value)
        return next_value
    
    def __str__(self):
        return '  '.join([str(val) for val in self.values])
    
    def __repr__(self):
        return str(self)

stack = []

if __name__ == '__main__':
    #lines = open('sample').read().split('\n')
    #lines = open('input').read().split('\n')
    lines = open('single').read().split('\n')
    rows = [Row(line) for line in lines]
    print(f'Number of rows: {len(rows)}')
    increment = 0
    stack.append(rows[0])
    for i,row in enumerate(rows):
        next_value = row.expand()
        print(f'row: {i} extrapolated value of {next_value}')
        increment += next_value
    #stack.append(rows[0])
    print(f'historic increment: {increment}')
    py = open('pyramid').read().split('\n')
    #for i,row in enumerate(stack[::-1]):
    for i,row in enumerate(stack):
        print(py[i])
        print(f'{i+1}.  {row}')
