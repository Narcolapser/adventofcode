import unittest
from main import check_row, expand_galaxy, pivot, find_pairs, find_distance

class TestExpansion(unittest.TestCase):
    def setUp(self):
        f = open('sample')
        self.galaxy = f.read().split('\n')
        f.close()

    def test_check_row(self):
        self.assertTrue(check_row(self.galaxy[0]))
        self.assertTrue(check_row(self.galaxy[1]))
        self.assertTrue(check_row(self.galaxy[2]))
        self.assertFalse(check_row(self.galaxy[3]))
    
    def test_pivot(self):
        input = [
            '....',
            '.#..',
            '#..#'
        ]
        pivoted = [
            '..#',
            '.#.',
            '...',
            '..#'
        ]
        self.assertEqual(pivot(input),pivoted)
    
    def test_expand_galaxy(self):
        f = open('sample.expanded')
        expanded = f.read().split('\n')
        f.close()
        self.assertEqual(expand_galaxy(self.galaxy), expanded)
    
    def test_get_pairs(self):
        self.assertEqual(len(find_pairs(self.galaxy)), 36)
    
    def test_get_distance(self):
        s1 = (6,1)
        s2 = (12,5)
        distance = find_distance(s1,s2)
        self.assertEqual(distance,9)

        s1 = (12,0)
        s2 = (12,5)
        distance = find_distance(s1,s2)
        self.assertEqual(distance,5)

        s1 = (2,0)
        s2 = (7,13)
        distance = find_distance(s1,s2)
        self.assertEqual(distance,17)

if __name__ == '__main__':
    unittest.main()