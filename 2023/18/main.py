class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def cast_ray(self,direction):
        return Ray(self,direction)
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def get_neighbors(self):
        n = []
        for i in (-0.5,0.5):
            for j in (-0.5,0.5):
                n.append(Point(self.x+i,self.y+j))
        return n
    
    def radiate(self):
        return [self.cast_ray(d) for d in ['u','d','l','r']]
    
    def __repr__(self):
        return f'({self.x},{self.y})'

class Ray:
    def __init__(self,point,direction):
        self.point = point
        self.direction = direction
    
    def __eq__(self,other):
        return self.direction == other.direction and self.point == other.point

class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __eq__(self,other):
        return self.start == other.start and self.end == other.end
    
    def orientation(self):
        if self.start == self.end:
            return False
        elif self.start.x == self.end.x:
            return 'v'
        elif self.start.y == self.end.y:
            return 'h'
        else:
            return False

    def intersect_ray(self,ray):
        # Parallel will not intersect:
        if self.orientation() == 'v' and ray.direction in ['u','d']:
            return False
        if self.orientation() == 'h' and ray.direction in ['r','l']:
            return False
        
        # We aren't paralle, lets see if the ray is between the beginning and the end.
        if self.orientation() == 'h':
            lowest = min(self.start.x, self.end.x)
            highest = max(self.start.x, self.end.x)
            if ray.point.x < lowest or ray.point.x > highest:
                return False

            # Ray is inside, is it looking at us?
            if ray.direction == 'u':
                return ray.point.y < self.start.y

        if self.orientation() == 'v':
            lowest = min(self.start.y, self.end.y)
            highest = max(self.start.y, self.end.y)
            if ray.point.y < lowest or ray.point.y > highest:
                return False
            
            # Ray is inside, is it looking at us?
            if ray.direction == 'r':
                return ray.point.x < self.start.x
        

class Poly:
    def __init__(self,lines):
        self.lines = lines

    def __contains__(self,point):
        if not isinstance(point,Point):
            return False
        
        # First get the neighbors
        neighbors = point.get_neighbors()

        # Next check each one to see if any of them are inside. If one is return true.
        for n in neighbors:
            # To see if an individual point is inside, we have it radiate
            # Here is a trick, if any one of them is true, they'll all be true, and vice versa. We actually only need one.
            # rays = n.radiate()
            ray = n.cast_ray('u')
            
            # Now that we have the ray. See how many lines that ray intersects.
            line_count = 0
            for line in self.lines:
                line_count += 1 if line.intersect_ray(ray) else 0

            # If the number of intersections is odd, we are inside.
            if line_count % 2 == 1:            
                return True
            
        return False

if __name__ == '__main__':
    instructions = open('sample').read().split('\n')
    instructions = open('input').read().split('\n')
    x = 0
    y = 0
    x_max = 0
    x_min = 0
    y_max = 0
    y_min = 0
    lines = []
    start = None
    end = Point(x,y)
    for instruction in instructions:
        direction, distance, _ = instruction.split(' ')
        # New line starts at the previous line's end.
        start = end
        if direction == 'U':
            y -= int(distance)
        elif direction == 'D':
            y += int(distance)
        elif direction == 'R':
            x += int(distance)
        elif direction == 'L':
            x -= int(distance)
        else:
            print(f'error, do not recognize direction {direction}')
        end = Point(x,y)
        x_max = max(x,x_max)
        x_min = min(x,x_min)
        y_max = max(y,y_max)
        y_min = min(y,y_min)
        lines.append(Line(start,end))
    poly = Poly(lines)
    print(f'x_max = {x_max} x_min = {x_min} y_max = {y_max} y_min = {y_min}')

    fill_count = 0
    # Scan through a square of points and see if we can find which or contained
    for y in range(y_min,y_max+1):
        for x in range(x_min,x_max+1):
            if Point(x,y) in poly:
                print('#',end='')
                fill_count += 1
            else:
                print('.',end='')
        print()

    print(f'Total number of blocks trenched: {fill_count}')