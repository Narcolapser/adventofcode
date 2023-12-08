import unittest
from d07 import Hand, Hand_Types

class Test_Range(unittest.TestCase):
    def test_hand_type(self):
        fiver = Hand('AAAAA')
        four = Hand('AA8AA')
        full = Hand('23332')
        three = Hand('TTT98')
        twopair = Hand('23432')
        onepair = Hand('A23A4')
        highcard = Hand('23456')
        self.assertEqual(fiver.get_type(),Hand_Types.FIVE_OF_A_KIND)
        self.assertEqual(four.get_type(),Hand_Types.FOUR_OF_A_KIND)
        self.assertEqual(full.get_type(),Hand_Types.FULL_HOUSE)
        self.assertEqual(three.get_type(),Hand_Types.THREE_OF_A_KIND)
        self.assertEqual(twopair.get_type(),Hand_Types.TWO_PAIR)
        self.assertEqual(onepair.get_type(),Hand_Types.ONE_PAIR)
        self.assertEqual(highcard.get_type(),Hand_Types.HIGH_CARD)

    def test_hand_value(self):
        hand = Hand('KK677')
        self.assertEqual(hand.get_value(),34040060707)
    
    def test_hand_compare(self):
        hand1 = Hand('32T3K')
        hand2 = Hand('KTJJT')
        hand3 = Hand('KK677')
        hand4 = Hand('T55J5')
        hand5 = Hand('QQQJA')

        self.assertTrue(hand1 < hand2)
        self.assertTrue(hand1 < hand3)
        self.assertTrue(hand1 < hand4)
        self.assertTrue(hand1 < hand5)

        self.assertTrue(hand2 > hand1)
        self.assertTrue(hand2 < hand3)
        self.assertTrue(hand2 < hand4)
        self.assertTrue(hand2 < hand5)

        self.assertTrue(hand3 > hand1)
        self.assertTrue(hand3 > hand2)
        self.assertTrue(hand3 < hand4)
        self.assertTrue(hand3 < hand5)

        self.assertTrue(hand4 > hand1)
        self.assertTrue(hand4 > hand2)
        self.assertTrue(hand4 > hand3)
        self.assertTrue(hand4 < hand5)

        self.assertTrue(hand5 > hand1)
        self.assertTrue(hand5 > hand2)
        self.assertTrue(hand5 > hand3)
        self.assertTrue(hand5 > hand4)

        self.assertTrue(hand1 == Hand('32T3K'))
        self.assertTrue(hand2 == Hand('KTJJT'))
        self.assertTrue(hand3 == Hand('KK677'))
        self.assertTrue(hand4 == Hand('T55J5'))
        self.assertTrue(hand5 == Hand('QQQJA'))
    
    def test_sorting(self):
        hand1 = Hand('32T3K')
        hand2 = Hand('KTJJT')
        hand3 = Hand('KK677')
        hand4 = Hand('T55J5')
        hand5 = Hand('QQQJA')

        disarray = [hand2, hand3, hand1, hand5, hand4]
        disarray.sort()
        self.assertEqual(disarray[0],hand1)
        self.assertEqual(disarray[1],hand2)
        self.assertEqual(disarray[2],hand3)
        self.assertEqual(disarray[3],hand4)
        self.assertEqual(disarray[4],hand5)

if __name__ == '__main__':
    unittest.main()