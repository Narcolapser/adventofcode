def create_square(char):
    if char == '.':
        return EmptySquare(char)
    if char == '\\':
        return Left_Mirror(char)
    if char == '/':
        return Right_Mirror(char)
    if char == '-':
        return Horizontal_Splitter(char)
    if char == '|':
        return Vertical_Splitter(char)

class Square():
    def __init__(self,char):
        self.char = char
        self.energized = False
        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.sent = set()
    
    def strike(self,direction):
        self.energized = True
    
    def set_neighbor(self,neighbor,direction):
        if direction == 'u':
            self.up = neighbor
        elif direction == 'd':
            self.down = neighbor
        elif direction == 'r':
            self.right = neighbor
        elif direction == 'l':
            self.left = neighbor
        else:
            return False
        return True

    def send(self,direction):
        if direction in self.sent:
            # Do not resend or we get an infinite loop.
            return
        self.sent.add(direction)
        if direction == 'u' and self.up:
            self.up.strike('d')
        elif direction == 'd' and self.down:
            self.down.strike('u')
        elif direction == 'r' and self.right:
            self.right.strike('l')
        elif direction == 'l' and self.left:
            self.left.strike('r')

class EmptySquare(Square):
    def strike(self,direction):
        super().strike(direction)
        if direction == 'l':
            self.send('r')
        if direction == 'r':
            self.send('l')
        if direction == 'u':
            self.send('d')
        if direction == 'd':
            self.send('u')

class Left_Mirror(Square):
    def strike(self,direction):
        super().strike(direction)
        if direction == 'l':
            self.send('d')
        if direction == 'r':
            self.send('u')
        if direction == 'u':
            self.send('r')
        if direction == 'd':
            self.send('l')

class Right_Mirror(Square):
    def strike(self,direction):
        super().strike(direction)
        if direction == 'l':
            self.send('u')
        if direction == 'r':
            self.send('d')
        if direction == 'u':
            self.send('l')
        if direction == 'd':
            self.send('r')
    
class Horizontal_Splitter(Square):
    def strike(self,direction):
        super().strike(direction)
        if direction in ['u','d']:
            self.send('l')
            self.send('r')
        if direction == 'l':
            self.send('r')
        if direction == 'r':
            self.send('l')
    
class Vertical_Splitter(Square):
    def strike(self,direction):
        super().strike(direction)
        if direction in ['l','r']:
            self.send('u')
            self.send('d')
        if direction == 'u':
            self.send('d')
        if direction == 'd':
            self.send('u')

if __name__ == '__main__':
    lines = open('input').read().split('\n')
    rows = []
    for line in lines:
        row = [create_square(c) for c in line]
        rows.append(row)
    
    # We now need to connect the mirrors to each other. First link horizontally
    for row in rows:
        cursor = 0
        while cursor < len(row) - 1:
            left = row[cursor]
            right = row[cursor+1]
            left.set_neighbor(right,'r')
            right.set_neighbor(left,'l')
            cursor += 1
        
    # Next link verically
    cursor = 0
    while cursor < len(rows[0]):
        for i,row in enumerate(rows[:-1]):
            upper = rows[i][cursor]
            lower = rows[i+1][cursor]
            upper.set_neighbor(lower,'d')
            lower.set_neighbor(upper,'u')
        cursor += 1
    
    # Strike the top left from the left
    rows[0][0].strike('l')
    
    # Count how many were energized.
    energized = []
    for row in rows:
        energized.append(sum([s.energized for s in row]))
    print(sum(energized))