import unittest
from main import FlipFlop, Conjunction

class TestFlipflow(unittest.TestCase):
    def test_flipflop_parse(self):
        line = '%sk -> rg, hh, hv, kr, kh, zl, zn'
        ff = FlipFlop(line)
        self.assertEqual(ff.name,'sk')
        self.assertEqual(ff.outputs,['rg','hh','hv','kr','kh','zl','zn'])
        self.assertEqual(ff.state,False)
    
    def test_handle_signal(self):
        line = '%sk -> rg, hh'
        ff = FlipFlop(line)

        self.assertEqual(ff.state,False)
        new_signals = ff.signal(('sk',True,'rg'))
        self.assertEqual(ff.state,False)
        self.assertEqual(len(new_signals), 0)

        new_signals = ff.signal(('sk',False,'rg'))
        self.assertEqual(ff.state,True)
        self.assertEqual(len(new_signals), 2)
        self.assertEqual(new_signals[0],('sk',True,'rg'))
        self.assertEqual(new_signals[1],('sk',True,'hh'))

        new_signals = ff.signal(('sk',True,'rg'))
        self.assertEqual(ff.state,True)
        self.assertEqual(len(new_signals), 0)

        new_signals = ff.signal(('sk',False,'rg'))
        self.assertEqual(ff.state,False)
        self.assertEqual(len(new_signals), 2)
        self.assertEqual(new_signals[0],('sk',False,'rg'))
        self.assertEqual(new_signals[1],('sk',False,'hh'))

class TestConjuction(unittest.TestCase):
    def test_conjuction_parse(self):
        line = '&sk -> rg, hh, hv, kr, kh, zl, zn'
        c = Conjunction(line)
        self.assertEqual(c.name,'sk')
        self.assertEqual(c.outputs,['rg','hh','hv','kr','kh','zl','zn'])

    def test_conjuction_signal(self):
        line = '%sk -> rg, hh'
        c = Conjunction(line)

        ns = c.signal(('i1',False,'rg'))
        self.assertEqual(ns[0],('sk',True,'rg'))
        self.assertEqual(ns[1],('sk',True,'hh'))

        ns = c.signal(('i1',True,'rg'))
        self.assertEqual(ns[0],('sk',False,'rg'))
        self.assertEqual(ns[1],('sk',False,'hh'))


        ns = c.signal(('i1',False,'rg'))
        self.assertEqual(ns[0],('sk',True,'rg'))
        self.assertEqual(ns[1],('sk',True,'hh'))
        ns = c.signal(('i2',True,'sk'))
        self.assertEqual(ns[0],('sk',True,'rg'))
        self.assertEqual(ns[1],('sk',True,'hh'))
        ns = c.signal(('i1',True,'rg'))
        self.assertEqual(ns[0],('sk',False,'rg'))
        self.assertEqual(ns[1],('sk',False,'hh'))
        

if __name__ == '__main__':
    unittest.main()
