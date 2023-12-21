class CMod():
    def __init__(self,line):
        self.name = line[1:3].strip(' ')
        self.outputs = line[7:].split(', ')

class FlipFlop(CMod):
    def __init__(self,line):
        super().__init__(line)
        self.state = False
    
    def signal(self,signal):
        if signal[1] == False:
            self.state = not self.state
            return [(self.name,self.state,output) for output in self.outputs]
        else:
            return []

class Conjunction(CMod):
    def __init__(self,line):
        super().__init__(line)
        self.memory = {}
    
    def signal(self,signal):
        self.memory[signal[0]] = signal[1]
        allhigh = all([self.memory[i] for i in self.memory])
        if allhigh:
            return [(self.name,False,output) for output in self.outputs]
        else:
            return [(self.name,True,output) for output in self.outputs]

if __name__ == '__main__':
    lines = open('input').read().split('\n')
    ffs = [FlipFlop(line) for line in lines if '%' in line]
    cons = [Conjunction(line) for line in lines if '&' in line]
    b_line = [line for line in lines if 'broadcaster' in line][0]
    initial_signals = [('br',False,i) for i in b_line.split(' -> ')[1].split(', ')]
    mods = {i.name:i for i in ffs+cons}
    high_sigs = 0
    low_sigs = 0
    for i in range(1):
        signals = [i for i in initial_signals]
        while len(signals):
            print(f'Current signal queue: {len(signals)}  sig_count {high_sigs,low_sigs}',end='\r')
            signal = signals.pop(0)
            if signal[1]:
                high_sigs +=1
            else:
                low_sigs += 1
            new_signals = mods[signal[2]].signal(signal)
            signals = signals + new_signals
            print(new_signals, signals)
    print()
    print(high_sigs*low_sigs)
