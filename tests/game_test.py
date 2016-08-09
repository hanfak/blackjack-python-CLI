import unittest
from mock import MagicMock
import mock
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.blackjack = Game()

    def test_0(self):
        """Only cards from 1 to 10 exist"""
        self.assertListEqual(self.blackjack.cards, [1,2,3,4,5,6,7,8,9,10])

    def test_1(self):
        """Player dealt winning cards"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,8])
        self.blackjack.deal()

        self.assertTrue(self.blackjack.is_winner())

    def test_2(self):
        """Player dealt losing hand"""
        self.blackjack.pick_cards = MagicMock(return_value=[1,7])
        self.blackjack.deal()

        self.assertFalse(self.blackjack.deal())

    def test_3(self):
        """When card is dealt, removed from pack"""
        self.blackjack.deal()

        self.assertEqual(len(self.blackjack.cards), 9)
        self.assertFalse(self.blackjack.hand[0] in self.blackjack.cards)
