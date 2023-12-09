import unittest
from d08 import link_to_bits

class Test_Helpers(unittest.TestCase):
    def test_link_to_bits(self):
        result = link_to_bits('AAA = (BBB, BBB)')
        self.assertEqual(result,['AAA','BBB','BBB'])
        

        result = link_to_bits('CCC = (ZZZ, GGG)')
        self.assertEqual(result,['CCC','ZZZ','GGG'])
        


if __name__ == '__main__':
    unittest.main()