import unittest
from d05 import Range, RangeMap

class Test_Range(unittest.TestCase):
    def test_line_parse(self):
        r = Range('50 98 2')
        self.assertEqual(r.destination, 50)
        self.assertEqual(r.source, 98)
        self.assertEqual(r.range, 2)

        r = Range('52 50 48')
        self.assertEqual(r.destination, 52)
        self.assertEqual(r.source, 50)
        self.assertEqual(r.range, 48)
    
    def test_range_find(self):
        r = Range('50 98 2')
        self.assertTrue(98 in r)
        self.assertTrue(99 in r)
        self.assertFalse(50 in r)

        r = Range('52 50 48')
        self.assertTrue(50 in r)
        self.assertTrue(51 in r)
        self.assertTrue(96 in r)
        self.assertTrue(97 in r)
        self.assertFalse(98 in r)

    def test_mapping(self):
        r = Range('52 50 48')
        self.assertEquals(r.map(50),52)
        self.assertEquals(r.map(51),53)
        self.assertEquals(r.map(96),98)
        self.assertEquals(r.map(97),99)
        self.assertFalse(r.map(98))

    def test_range_map(self):
        rm = RangeMap([Range('50 98 2'), Range('52 50 48')])
        self.assertEquals(rm.map(1),1)
        self.assertEquals(rm.map(49),49)
        self.assertEquals(rm.map(51),53)
        self.assertEquals(rm.map(96),98)
        self.assertEquals(rm.map(97),99)
        self.assertEquals(rm.map(98),50)
        self.assertEquals(rm.map(99),51)

if __name__ == '__main__':
    unittest.main()