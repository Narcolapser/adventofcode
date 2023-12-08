card_map = {
    'A':'50',
    'K':'40',
    'Q':'30',
    'J':'20',
    'T':'10',
    '9':'09',
    '8':'08',
    '7':'07',
    '6':'06',
    '5':'05',
    '4':'04',
    '3':'03',
    '2':'02'
}

joker_map = {
    'A':'50',
    'K':'40',
    'Q':'30',
    'J':'01',
    'T':'10',
    '9':'09',
    '8':'08',
    '7':'07',
    '6':'06',
    '5':'05',
    '4':'04',
    '3':'03',
    '2':'02'
}

class Hand_Types():
    '''
    This class is a mapping of hand types to their relative ranks.
    '''
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

class Hand():
    def __init__(self,hand):
        self.hand = hand
    
    def get_type(self):
        # Make a set of the cards. This is useful for all of the possible configurations.
        hand_set = set(self.hand)

        # Test 5 of a kind
        if len(hand_set) == 1:
            # All the cards were the same. Can only mean 5 of a kind.
            return Hand_Types.FIVE_OF_A_KIND

        # Make a dictionary of how many matches there are of each card. This is useful for finding sets.
        matches = {card:0 for card in hand_set}
        for card in self.hand:
            matches[card] += 1
        
        # Find the largest set
        largest = max(matches.values())

        # Test 4 and full house
        if len(hand_set) == 2:
            # with only 2 distinct cards, there is either 4 and 1 or 2 and 3. 
            if largest == 4:
                return Hand_Types.FOUR_OF_A_KIND
            else:
                return Hand_Types.FULL_HOUSE
        
        # Test for 3 of a kind and 2 pair
        if len(hand_set) == 3:
            # with 3 different cards we either have 3 matched and two singles. or two pairs and one single.
            if largest == 3:
                return Hand_Types.THREE_OF_A_KIND
            else:
                return Hand_Types.TWO_PAIR
        
        # Check for a single pair. 
        if len(hand_set) == 4:
            # 4 distinct cards means there is one card that is doubled.
            return Hand_Types.ONE_PAIR
        
        # The only remaining option is no sets, so high card.
        return Hand_Types.HIGH_CARD

    def get_value(self):
        value = str(self.get_type())
        for card in self.hand:
            value += card_map[card]
        return int(value)
    
    def __gt__(self,other):
        my_value = self.get_value()
        other_value = other.get_value()
        return my_value > other_value
    
    def __eq__(self,other):
        my_value = self.get_value()
        other_value = other.get_value()
        return my_value == other_value

class JokerHand(Hand):
    def get_value(self):
        value = str(self.get_type())
        for card in self.hand:
            value += joker_map[card]
        return int(value)
    
    def get_type(self):
        # If there are no jokers in the hand, grade as usual.
        if 'J' not in self.hand:
            return super().get_type()
        
        # Remove jokers from the hand.
        jokerless = self.hand.replace('J','')
        
        # Make a set of the cards. This is useful for all of the possible configurations.
        hand_set = set(jokerless)
        print(f'Jokerless hand: {jokerless} and set {hand_set}')

        # Test 5 of a kind
        if len(hand_set) == 1:
            # All non jokers were the same. Lets make 5 of a kind.
            return Hand_Types.FIVE_OF_A_KIND
        
        # Make a dictionary of how many matches there are of each card. This is useful for finding sets.
        matches = {card:0 for card in hand_set}
        for card in jokerless:
            matches[card] += 1
        
        # Find the largest set
        largest = max(matches.values())

        # if we have 3 of a kind we could do full house or 4 of a kind. The former is higher ranked so we will always choose it.
        if largest == 3:
            return Hand_Types.FOUR_OF_A_KIND
        
        # If we have two pair, the best we can get from it is a full house.
        if largest == 2 and len(hand_set) == 2:
            return Hand_Types.FULL_HOUSE
        
        # If we a single pair we could do 3 of a kind or 2 pair. again, the former is higher ranked so we will always choose it.
        if largest == 2:
            return Hand_Types.THREE_OF_A_KIND
        
        # At this point we have 4 disjointed cards. The best we can manage is two pair.
        return Hand_Types.TWO_PAIR

        


if __name__ == '__main__':
    lines = open('d07.sample').read().split('\n')
    lines = open('d07.input').read().split('\n')
    hands = [Hand(line.split(' ')[0]) for line in lines]
    bids = { line.split(' ')[0]:int(line.split(' ')[1]) for line in lines }
    hands.sort()
    total_winnings = 0
    for hand in hands:
        print(f'hand {hand.hand} position: {hands.index(hand)}')
        rank = hands.index(hand) + 1
        total_winnings += bids[hand.hand] * rank
    print(f'Total winnings: {total_winnings}')