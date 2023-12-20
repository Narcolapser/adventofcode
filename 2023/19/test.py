import unittest
from main import Part, Workflow, Rule

class TestPart(unittest.TestCase):
    def test_line_parse(self):
        line = '{x=787,m=2655,a=1222,s=2876}'
        part = Part(line)
        self.assertEqual(part.x,787)
        self.assertEqual(part.m,2655)
        self.assertEqual(part.a,1222)
        self.assertEqual(part.s,2876)
        self.assertEqual(part.visited,set())

    def test_part_value(self):
        p1 = Part('{x=787,m=2655,a=1222,s=2876}')
        p3 = Part('{x=2036,m=264,a=79,s=2244}')
        p5 = Part('{x=2127,m=1623,a=2188,s=1013}')

        self.assertEqual(p1.value,7540)
        self.assertEqual(p3.value,4623)
        self.assertEqual(p5.value,6951)
        

class TestWorkflow(unittest.TestCase):
    def test_workflow_parse(self):
        line = 'px{a<2006:qkq,m>2090:A,rfg}'
        wf = Workflow(line)
        self.assertEqual(wf.name, 'px')
        self.assertEqual(len(wf.rules), 3)
    
    def test_call_workflow(self):
        wf = Workflow('px{a<2006:qkq,m>2090:A,rfg}')
        p1 = Part('{x=787,m=255,a=222,s=2876}')
        p2 = Part('{x=787,m=2665,a=6222,s=2876}')
        p3 = Part('{x=787,m=255,a=6222,s=2876}')

        self.assertEqual(wf(p1),'qkq')
        self.assertEqual(wf(p2),'A')
        self.assertEqual(wf(p3),'rfg')

class TestRule(unittest.TestCase):
    def test_rule_parse(self):
        line = 'a<2006:qkq'
        r = Rule(line)
        self.assertEqual(r.part, 'a')
        self.assertEqual(r.operator, '<')
        self.assertEqual(r.value, 2006)
        self.assertEqual(r.action, 'qkq')

        shortline = 'A'
        r = Rule(shortline)
        self.assertEqual(r.action,'A')
        self.assertIsNone(r.part)
        self.assertIsNone(r.operator)
        self.assertIsNone(r.value)
    
    def test_call_rule(self):
        line = '{x=787,m=2655,a=1222,s=2876}'
        part = Part(line)

        r1 = Rule('x<2006:r1')
        r2 = Rule('m>206:r2')
        r3 = Rule('a<648:r3')
        r4 = Rule('s>1155:r4')
        r5 = Rule('A')

        self.assertTrue( r1(part))
        self.assertTrue( r2(part))
        self.assertFalse(r3(part))
        self.assertTrue( r4(part))
        self.assertTrue( r5(part))

        part.visited = {'r1','r2','r3'}

        self.assertFalse( r1(part))
        self.assertFalse( r2(part))
        self.assertFalse(r3(part))



if __name__ == '__main__':
    unittest.main()