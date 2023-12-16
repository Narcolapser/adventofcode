import unittest
from main import hash_string, hash_line

class TestHash(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(hash_string('HASH'),52)
    
    def test_hash_line(self):
        line = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
        self.assertEqual(hash_line(line),1320)

if __name__ == '__main__':
    unittest.main()