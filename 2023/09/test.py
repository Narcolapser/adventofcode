import unittest
from main import Row

class TestRow(unittest.TestCase):
    def test_predict_next_0(self):
        r = Row('0 0 0 0')
        predicted = r.predict(5)
        self.assertEqual(predicted,0)

    def test_predict_non_zero(self):
        r = Row('2 2 2 2')
        predicted = r.predict(0)
        self.assertEqual(predicted, 2)

        r = Row('0 2 4 6')
        predicted = r.predict(2)
        self.assertEqual(predicted, 8)

        r = Row('3 3 5 9 15')
        predicted = r.predict(8)
        self.assertEqual(predicted, 23)

        r = Row('10 13 16 21 30 45')
        predicted = r.predict(23)
        self.assertEqual(predicted, 68)
    
    def test_compare_row(self):
        r1 = Row('2 2 2 2')
        r2 = Row('2 2 2 2')
        r3 = Row('1 2 3 4')

        self.assertTrue(r1 == r2)
        self.assertFalse(r2 == r3)
        self.assertFalse(r1 == r3)
    
    def test_get_next_row(self):
        r = Row('10 13 16 21 30 45')
        decendant = r.get_descendant()
        self.assertTrue(Row('3 3 5 9 15') == decendant)

        r = Row('1   3   6  10  15  21')
        decendant = r.get_descendant()
        next_row = Row('2   3   4   5   6')
        self.assertTrue(decendant == next_row)
        
        r = next_row
        decendant = r.get_descendant()
        next_row = Row('1  1 1 1')
        self.assertTrue(decendant == next_row)

        r = next_row
        decendant = r.get_descendant()
        next_row = Row('0 0 0')
        self.assertTrue(decendant == next_row)

        self.assertFalse(next_row.get_descendant())
    
    def test_get_next_row_bigger(self):
        r = Row('8  31  64  97  122  140  166  230  372  629  1012  1471  1846  1802')
        descendant = r.get_descendant()
        comp = Row('23  33  33  25  18  26  64  142  257  383  459  375  -44')
        self.assertTrue(descendant == comp)
    
    def test_expand(self):
        start = Row('0   3   6   9  12  15')
        end = Row('0   3   6   9  12  15  18')
        expand_value = start.expand()
        self.assertEqual(expand_value, 18)
        self.assertTrue(end == start)

    def test_parse(self):
        row = Row('23  33  33  25  18  26  64  142  257  383  459  375  -44')
        values = [23, 33, 33, 25, 18, 26, 64, 142, 257, 383, 459, 375, -44]
        self.assertEqual(row.values,values)

if __name__ == '__main__':
    unittest.main()
