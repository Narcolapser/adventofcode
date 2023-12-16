import unittest
from main import create_square, Square, Left_Mirror, Right_Mirror, Horizontal_Splitter, Vertical_Splitter, EmptySquare

class TestSquare(unittest.TestCase):
    def test_creation(self):
        s = create_square('.')
        self.assertTrue(isinstance(s,EmptySquare))

        s = create_square('/')
        self.assertTrue(isinstance(s,Right_Mirror))

        s = create_square('\\')
        self.assertTrue(isinstance(s,Left_Mirror))

        s = create_square('-')
        self.assertTrue(isinstance(s,Horizontal_Splitter))

        s = create_square('|')
        self.assertTrue(isinstance(s,Vertical_Splitter))

    def test_energize(self):
        s = Square('.')
        self.assertFalse(s.energized)
        s.strike('l')
        self.assertTrue(s.energized)

    def test_set_neighbor(self):
        central = Square('|')
        upper = Square('.')
        lower = Square('/')

        central.set_neighbor(upper,'u')
        central.set_neighbor(lower,'d')
        upper.set_neighbor(central,'d')
        lower.set_neighbor(central,'u')

        self.assertEqual(central.up,upper)
        self.assertEqual(central.down,lower)

        self.assertEqual(upper.down,central)
        self.assertEqual(lower.up,central)
    
    def test_Left_Mirror(self):
        s = create_square('\\')

        u = create_square('.')
        d = create_square('.')
        l = create_square('.')
        r = create_square('.')

        s.set_neighbor(u,'u')
        s.set_neighbor(d,'d')
        s.set_neighbor(l,'l')
        s.set_neighbor(r,'r')

        # Starting no body is energized.
        self.assertFalse(any([n.energized for n in [u,d,l,r,s]]))

        # From the left
        s.strike('l')
        self.assertFalse(any([n.energized for n in [u,l,r]]))
        self.assertTrue(all([n.energized for n in [s,d]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the right
        s.strike('r')
        self.assertFalse(any([n.energized for n in [d,l,r]]))
        self.assertTrue(all([n.energized for n in [s,u]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the up
        s.strike('u')
        self.assertFalse(any([n.energized for n in [u,l,d]]))
        self.assertTrue(all([n.energized for n in [s,r]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the down
        s.strike('d')
        self.assertFalse(any([n.energized for n in [u,d,r]]))
        self.assertTrue(all([n.energized for n in [s,l]]))
        for n in [u,d,l,r,s]: n.energized = False
    
    def test_Right_Mirror(self):
        s = create_square('/')

        u = create_square('.')
        d = create_square('.')
        l = create_square('.')
        r = create_square('.')

        s.set_neighbor(u,'u')
        s.set_neighbor(d,'d')
        s.set_neighbor(l,'l')
        s.set_neighbor(r,'r')

        # Starting no body is energized.
        self.assertFalse(any([n.energized for n in [u,d,l,r,s]]))

        # From the left
        s.strike('l')
        self.assertFalse(any([n.energized for n in [d,l,r]]))
        self.assertTrue(all([n.energized for n in [s,u]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the right
        s.strike('r')
        self.assertFalse(any([n.energized for n in [u,l,r]]))
        self.assertTrue(all([n.energized for n in [s,d]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the up
        s.strike('u')
        self.assertFalse(any([n.energized for n in [u,r,d]]))
        self.assertTrue(all([n.energized for n in [s,l]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the down
        s.strike('d')
        self.assertFalse(any([n.energized for n in [u,d,l]]))
        self.assertTrue(all([n.energized for n in [s,r]]))
    
    def test_VSplit(self):
        s = create_square('|')

        u = create_square('.')
        d = create_square('.')
        l = create_square('.')
        r = create_square('.')

        s.set_neighbor(u,'u')
        s.set_neighbor(d,'d')
        s.set_neighbor(l,'l')
        s.set_neighbor(r,'r')

        # Starting no body is energized.
        self.assertFalse(any([n.energized for n in [u,d,l,r,s]]))

        # From the left
        s.strike('l')
        self.assertFalse(any([n.energized for n in [l,r]]))
        self.assertTrue(all([n.energized for n in [s,d,u]]))
        for n in [u,d,l,r,s]: n.energized = False
        s.sent = set()

        # From the right
        s.strike('r')
        self.assertFalse(any([n.energized for n in [l,r]]))
        self.assertTrue(all([n.energized for n in [s,d,u]]))
        for n in [u,d,l,r,s]: n.energized = False
        s.sent = set()

        # From the up
        s.strike('u')
        self.assertFalse(any([n.energized for n in [u,r,l]]))
        self.assertTrue(all([n.energized for n in [s,d]]))
        for n in [u,d,l,r,s]: n.energized = False
        s.sent = set()

        # From the down
        s.strike('d')
        self.assertFalse(any([n.energized for n in [r,d,l]]))
        self.assertTrue(all([n.energized for n in [s,u]]))
    
    def test_HSplit(self):
        s = create_square('-')

        u = create_square('.')
        d = create_square('.')
        l = create_square('.')
        r = create_square('.')

        s.set_neighbor(u,'u')
        s.set_neighbor(d,'d')
        s.set_neighbor(l,'l')
        s.set_neighbor(r,'r')

        # Starting no body is energized.
        self.assertFalse(any([n.energized for n in [u,d,l,r,s]]))

        # From the left
        s.strike('l')
        self.assertFalse(any([n.energized for n in [l,d,u]]))
        self.assertTrue(all([n.energized for n in [s,r]]))
        for n in [u,d,l,r,s]: n.energized = False
        s.sent = set()

        # From the right
        s.strike('r')
        self.assertFalse(any([n.energized for n in [d,u,r]]))
        self.assertTrue(all([n.energized for n in [s,l]]))
        for n in [u,d,l,r,s]: n.energized = False
        s.sent = set()

        # From the up
        s.strike('u')
        self.assertFalse(any([n.energized for n in [u,d]]))
        self.assertTrue(all([n.energized for n in [s,r,l]]))
        for n in [u,d,l,r,s]: n.energized = False
        s.sent = set()

        # From the down
        s.strike('d')
        self.assertFalse(any([n.energized for n in [d,u]]))
        self.assertTrue(all([n.energized for n in [s,r,l]]))
    
    def test_Right_Mirror(self):
        s = create_square('.')

        u = create_square('.')
        d = create_square('.')
        l = create_square('.')
        r = create_square('.')

        s.set_neighbor(u,'u')
        s.set_neighbor(d,'d')
        s.set_neighbor(l,'l')
        s.set_neighbor(r,'r')

        # Starting no body is energized.
        self.assertFalse(any([n.energized for n in [u,d,l,r,s]]))

        # From the left
        s.strike('l')
        self.assertFalse(any([n.energized for n in [d,u,l]]))
        self.assertTrue(all([n.energized for n in [s,r]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the right
        s.strike('r')
        self.assertFalse(any([n.energized for n in [u,r,d]]))
        self.assertTrue(all([n.energized for n in [s,l]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the up
        s.strike('u')
        self.assertFalse(any([n.energized for n in [l,r,u]]))
        self.assertTrue(all([n.energized for n in [s,d]]))
        for n in [u,d,l,r,s]: n.energized = False

        # From the down
        s.strike('d')
        self.assertFalse(any([n.energized for n in [d,r,l]]))
        self.assertTrue(all([n.energized for n in [s,u]]))


if __name__ == '__main__':
    unittest.main()