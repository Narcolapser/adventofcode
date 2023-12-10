import unittest
from main import NeighborFetcher, PathFinder, DirToPos, ForwardFinder

class TestPipes(unittest.TestCase):
    def setUp(self):
        f = open('sample2')
        self.maze = f.read().split('\n')
        f.close()
        
    def test_neighborfetcher(self):
        self.assertEqual(
            NeighborFetcher(self.maze,(0,0)),
            {'d':'.','r':'-'})
        
        self.assertEqual(
            NeighborFetcher(self.maze,(1,1)),
            {'l':'.','u':'-','r':'J','d':'J'})
        
        self.assertEqual(
            NeighborFetcher(self.maze,(4,4)),
            {'l':'L','u':'J'})
    
    def test_pathfinder(self):
        self.assertEqual(PathFinder({'d':'.','r':'-'},'-'),{'r'})
        self.assertEqual(PathFinder({'d':'|','r':'|'},'7'),{'d'})
        self.assertEqual(PathFinder({'u':'|','d':'7'},'L'),{'u'})
        self.assertEqual(PathFinder({'u':'L','l':'L'},'J'),{'l'})

        self.assertEqual(PathFinder({'u':'7','l':'L','d':'J'},'7'),{'l','d'})
        self.assertEqual(PathFinder({'r':'7','l':'-','d':'J'},'F'),{'d','l'})
    
    def test_dir_to_pos(self):
        self.assertEqual(DirToPos((1,1),'r'),(2,1))
        self.assertEqual(DirToPos((1,1),'l'),(0,1))
        self.assertEqual(DirToPos((1,1),'u'),(1,0))
        self.assertEqual(DirToPos((1,1),'d'),(1,2))
    
    def test_forward_finder(self):
        self.assertEqual(ForwardFinder({'l','u'},'d'),'l')
        self.assertEqual(ForwardFinder({'r','d'},'l'),'d')
        self.assertEqual(ForwardFinder({'d','u'},'u'),'u')
        self.assertEqual(ForwardFinder({'r','l'},'r'),'r')


if __name__ == '__main__':
    unittest.main()