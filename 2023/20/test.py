import unittest
from main import FlipFlop

class TestFlipflow(unittest.TestCase):
    def test_flipflop_parse(self):
        line = '&sk -> rg, hh, hv, kr, kh, zl, zn'
        ff = FlipFlop(line)
        self.assertEqual(ff.name,'sk')
        self.assertEqual(ff.outputs,['rg','hh','hv','kr','kh','zl','zn'])
        self.assertEqual(ff.state,False)
    
    def test_handle_signal(self):
        line = '&sk -> rg, hh'
        ff = FlipFlop(line)

        self.assertEqual(ff.state,False)
        new_signals = ff.signal(True)
        self.assertEqual(ff.state,False)
        self.assertEqual(len(new_signals), 0)

        new_signals = ff.signal(False)
        self.assertEqual(ff.state,True)
        self.assertEqual(len(new_signals), 2)
        self.assertEqual(new_signals[0],('rg',True))
        self.assertEqual(new_signals[1],('hh',True))

        new_signals = ff.signal(True)
        self.assertEqual(ff.state,True)
        self.assertEqual(len(new_signals), 0)

        new_signals = ff.signal(False)
        self.assertEqual(ff.state,False)
        self.assertEqual(len(new_signals), 2)
        self.assertEqual(new_signals[0],('rg',False))
        self.assertEqual(new_signals[1],('hh',False))

if __name__ == '__main__':
    unittest.main()
