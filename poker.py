"""
Some classes for working with Poker hands.
"""


class Card:

    values = tuple(map(int, (range(2, 11))))+('J', 'Q', 'K', 'A')
    suits = ('S', 'H', 'C', 'D')


    def __init__(self, value, suit):
        # check to make sure value and suit are legal
        self._value = value
        self._suit = suit

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return "{} of {}".format(self._value, self._suit)

class Deck:

    def __init__(self):

        self.cards = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + '\n'
        return s

class Hand(Deck):

    def __init__(self, cards):
        self.cards = cards

    def whatami(self):
        """ Return the type of hand as a lower-case string, e.g.,

            full house
            three-of-a-kind
            two pairs
            pair

        """

        my_type = 'pair'

        return my_type


if __name__ == '__main__':

    card = Card('2', 'D')
    print(card)


    deck = Deck()

    cards = deck.cards[4:9]

    hand = Hand(cards)
