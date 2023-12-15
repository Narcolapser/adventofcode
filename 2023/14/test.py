import unittest
from main import roll_row_north, weigh_row

class TestMain(unittest.TestCase):
    def test_Top(self):
        row = "O.O"
        north = None
        new_row, new_north = roll_row_north(row,north)
        self.assertEqual(new_row,row)
        self.assertEqual(north, new_north)

    def test_empty(self):
        row = "O.O"
        north = "..."
        new_row, new_north = roll_row_north(row,north)
        self.assertEqual(new_row, '...')
        self.assertEqual(new_north, 'O.O')

    def test_blocked(self):
        row = "OOO"
        north = "#O."
        new_row, new_north = roll_row_north(row,north)
        self.assertEqual(new_row, 'OO.')
        self.assertEqual(new_north, '#OO')
    
    def test_weigh_row(self):
        row = 'OOOO.#.O..'
        position = 10
        weight = weigh_row(row,position)
        self.assertEqual(weight,50)

        row = 'O..#.OO...'
        position = 7
        weight = weigh_row(row,position)
        self.assertEqual(weight,21)

if __name__ == '__main__':
    unittest.main()