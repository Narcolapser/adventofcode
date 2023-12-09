import unittest
from d05 import Range, RangeMap, MAX_INT

class Test_Range(unittest.TestCase):
    def setUp(self):
        f = open('d05.sample')
        segments = f.read().split('\n\n')
        f.close()
        maps = []
        for segment in segments[1:]:
            name = segment.split('\n')[0]
            ranges = [Range(line) for line in segment.split('\n')[1:] if ' ' in line]
            maps.append(RangeMap(name,ranges,None))

        self.rmap = maps.pop(0)
        cursor = self.rmap
        while len(maps):
            cursor.next_range = maps.pop(0)
            cursor = cursor.next_range
        

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
        self.assertEqual(r.map(50),52)
        self.assertEqual(r.map(51),53)
        self.assertEqual(r.map(96),98)
        self.assertEqual(r.map(97),99)
        self.assertFalse(r.map(98))

    def test_mapping_extended(self):
        r = Range('52 50 48')
        self.assertFalse(r.map_extended(49))
        self.assertEqual(r.map_extended(50),{'map':52,'more':47})
        self.assertEqual(r.map_extended(51),{'map':53,'more':46})
        self.assertEqual(r.map_extended(96),{'map':98,'more':1})
        self.assertEqual(r.map_extended(97),{'map':99,'more':0})
        self.assertFalse(r.map_extended(98))

    def test_range_map(self):
        rm = RangeMap('test',[Range('50 98 2'), Range('52 50 48')],None)
        self.assertEqual(rm.map(1),1)
        self.assertEqual(rm.map(49),49)
        self.assertEqual(rm.map(51),53)
        self.assertEqual(rm.map(96),98)
        self.assertEqual(rm.map(97),99)
        self.assertEqual(rm.map(98),50)
        self.assertEqual(rm.map(99),51)

    def test_range_map_range(self):
        rm = RangeMap('test',[Range('50 98 2'), Range('52 50 48')],None)
        self.assertEqual(rm.map_range(1),{'map':1,'more':49})
        self.assertEqual(rm.map_range(49),{'map':49,'more':1})
        self.assertEqual(rm.map_range(50),{'map':52,'more':47})
        self.assertEqual(rm.map_range(51),{'map':53,'more':46})
        self.assertEqual(rm.map_range(96),{'map':98,'more':1})
        self.assertEqual(rm.map_range(97),{'map':99,'more':0})
        self.assertEqual(rm.map_range(98),{'map':50,'more':1})
        self.assertEqual(rm.map_range(99),{'map':51,'more':0})
        self.assertEqual(rm.map_range(100),{'map':100,'more':MAX_INT})
        

    def test_range_linking(self):
        cursor = self.rmap
        count = 1
        while cursor.next_range:
            cursor = cursor.next_range
            count += 1
        self.assertEqual(count,7)

    def test_range_map_extended(self):
        self.assertEqual(self.rmap.map_extended(79)['map'],82)
        self.assertEqual(self.rmap.map_extended(14)['map'],43)
        self.assertEqual(self.rmap.map_extended(55)['map'],86)
        self.assertEqual(self.rmap.map_extended(13)['map'],35)

if __name__ == '__main__':
    unittest.main()