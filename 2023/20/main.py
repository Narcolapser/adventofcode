class FlipFlop():
    def __init__(self,line):
        self.name = line[1:3]
        self.outputs = line[7:].split(', ')
        self.state = False
    
    def signal(self,signal):
        if signal == False:
            self.state = not self.state
            return [(output,self.state) for output in self.outputs]
        else:
            return []
