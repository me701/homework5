from poker import *
import unittest

class TestPoker(unittest.TestCase):

    def test_pair(self):
        """ Ensures a pair is found.
        """

        pair = Hand([Card('2','H'),
                     Card('2','D'),
                     Card('3','H'),
                     Card('4','C'),
                     Card('6','S')])

        self.assertEqual(pair.whatami(), 'pair')

    def test_flush(self):
        """ Ensures a flush is found.
        """

        pair = Hand([Card('2','H'),
                     Card('3','H'),
                     Card('5','H'),
                     Card('7','H'),
                     Card('9','H')])

        self.assertEqual(pair.whatami(), 'flush')

if __name__ == '__main__':

    unittest.main()
