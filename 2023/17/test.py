import unittest
from main import get_position, check_final_pos, get_heat

class Test_Stuff(unittest.TestCase):
    def setUp(self):
        f = open('sample')
        self.city = f.read().split('\n')
        f.close()

    def test_get_pos(self):
        # Test top left corner
        position = (0,0)
        self.assertFalse(get_position(self.city,position,'u'))
        self.assertFalse(get_position(self.city,position,'l'))
        self.assertEqual(get_position(self.city,position,'r'),(1,0))
        self.assertEqual(get_position(self.city,position,'d'),(0,1))

        position = (len(self.city[0])-1,len(self.city)-1)
        self.assertFalse(get_position(self.city,position,'d'))
        self.assertFalse(get_position(self.city,position,'r'))
        self.assertEqual(get_position(self.city,position,'l'),(position[0]-1,position[1]))
        self.assertEqual(get_position(self.city,position,'u'),(position[0],position[1]-1))

    def test_check_final_pos(self):
        self.assertFalse(check_final_pos(self.city,(0,0)))
        self.assertFalse(check_final_pos(self.city,(1,0)))
        self.assertFalse(check_final_pos(self.city,(7,5)))
        self.assertTrue(check_final_pos(self.city,(13,13)))
    
    def test_get_heat(self):
        self.assertEqual(get_heat(self.city,(0,0)),'2')
        self.assertEqual(get_heat(self.city,(2,2)),'5')
        self.assertEqual(get_heat(self.city,(0,4)),'4')
        self.assertEqual(get_heat(self.city,(5,1)),'5')


if __name__ == '__main__':
    unittest.main()