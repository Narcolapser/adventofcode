class Part:
    x = None
    m = None
    a = None
    s = None
    visited: set[str] = None
    def __init__(self,line):
        x,m,a,s = line.strip('{').strip('}').split(',')
        self.x = int(x.split('=')[1])
        self.m = int(m.split('=')[1])
        self.a = int(a.split('=')[1])
        self.s = int(s.split('=')[1])
        self.visited = set()
    
    @property
    def value(self):
        return sum([self.x, self.a, self.m, self.s])

class Workflow:
    name = None
    rules = None
    def __init__(self,line):
        self.name, rules = line.strip('}').split('{')
        rules = rules.split(',')
        self.rules = [Rule(r) for r in rules]
    
    def __call__(self,part:Part):
        # Set the default rule
        matched_rule = self.rules[-1]
        for rule in self.rules:
            matched = rule(part)
            if matched:
                matched_rule = rule
                break
        
        # We now have the matched rule. Send up it's action.
        return matched_rule.action

class Rule:
    part = None
    operator = None
    value = None
    action = None
    def __init__(self,line):
        if ':' not in line:
            self.action = line
        else:
            self.part = line[0]
            self.operator = line[1]
            self.value = int(line[2:line.index(':')])
            self.action = line[line.index(':')+1:]
    
    def __repr__(self):
        if self.part:
            return f'({self.part} {self.operator} {self.value}) -> {self.action}'
        else:
            return f'--> {self.action}'
    
    def __call__(self, part:Part):
        # If we were not given a rule to work with, we are a default rule and so always evaluate true.
        if not self.part:
            return True

        matched = False
        if self.operator == '>':
            matched = getattr(part,self.part) > self.value
        else:
            matched = getattr(part,self.part) < self.value
        
        if matched:
            if self.action in part.visited:
                matched = False

        return matched

if __name__ == '__main__':
    wf_lines, part_lines = open('sample').read().split('\n\n')
    workflows = [Workflow(i) for i in wf_lines.split('\n')]
    workflow_dict = {w.name:w for w in workflows}
    parts = [Part(i) for i in part_lines.split('\n')]
    rejected = []
    accepted = []
    for part in parts:
        action = workflow_dict['in'](part)
        while action not in ['A','R']:
            action = workflow_dict[action](part)
        if action == 'A':
            accepted.append(part)
        else:
            rejected.append(part)
    
    value = sum([p.value for p in accepted])
    print(f'Sum of accepted parts: {value}')
