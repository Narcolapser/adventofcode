import unittest
from d03 import line_seek

# given a position in an line, identify if there are numbers in it or either side.
class Test_line_search(unittest.TestCase):
    def test_split_numbers(self):
        line = "..234.534.."
        result = line_seek(line,5)
        self.assertEqual(result[0],234)
        self.assertEqual(result[1],534)

    def test_joined_numbers(self):
        line = "..2349534.."
        result = line_seek(line,5)
        self.assertEqual(result[0],2349534)

    def test_joined_numbers(self):
        line = "........."
        result = line_seek(line,5)
        self.assertEqual(result,[])
    
    def test_left_to_edge(self):
        line = "123......"
        result = line_seek(line,3)
        self.assertEqual(result[0],123)
    
    def test_right_to_edge(self):
        line = "...456"
        result = line_seek(line,2)
        self.assertEqual(result[0],456)

if __name__ == '__main__':
    unittest.main()
