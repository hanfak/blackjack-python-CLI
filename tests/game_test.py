import unittest
from mock import MagicMock
import mock
from lib.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.blackjack = Game()

    def test_0(self):
        """Only cards from 1 to 10 exist"""
        self.assertListEqual(self.blackjack.cards, [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A'])

    def test_1a(self):
        """Player dealt winning cards"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,8])
        self.blackjack.deal()

        self.assertEqual(self.blackjack.points(), 18)

    def test_1b(self):
        """Player dealt losing hand"""
        self.blackjack.pick_cards = MagicMock(return_value=[2,7])
        self.blackjack.deal()

        self.assertFalse(self.blackjack.deal())

    def test_1c(self):
        """Player dealt cards from deck"""
        self.blackjack.pick_cards = MagicMock(return_value=[2,7])
        self.blackjack.deal()

        self.assertTrue(self.blackjack.hand[0] in self.blackjack.cards)
        self.assertTrue(self.blackjack.hand[1] in self.blackjack.cards)

    def test_2a(self):
        """When card is dealt, removed from pack"""
        self.blackjack.deal()

        self.assertEqual(len(self.blackjack.cards), 12)
        self.assertFalse(self.blackjack.hand[0] in self.blackjack.cards)

    def test_3a(self):
        """Can start new game, resets hand"""
        self.blackjack.deal()
        self.blackjack.new_game()

        self.assertEqual(self.blackjack.hand,[])

    def test_3b(self):
        """Can start new game, resets deck"""
        self.blackjack.deal()
        self.blackjack.new_game()

        self.assertEqual(self.blackjack.cards,[2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A'])

    def test_4a(self):
        """Include points for one face cards"""
        self.blackjack.pick_cards = MagicMock(return_value=['K',7])
        self.blackjack.deal()

        self.assertEqual(self.blackjack.points(),17)

    def test_4b(self):
        """Include points for two face cards"""
        self.blackjack.pick_cards = MagicMock(return_value=['K','J'])
        self.blackjack.deal()

        self.assertEqual(self.blackjack.points(),20)

    def test_5a(self):
        """include points where one card is an ace"""
        self.blackjack.pick_cards = MagicMock(return_value=['A',7])
        self.blackjack.deal()

        self.assertEqual(self.blackjack.points(), 18)

    def test_5b(self):
        """include points win with black jack"""
        self.blackjack.pick_cards = MagicMock(return_value=['K','A'])
        self.blackjack.deal()

        self.assertTrue(self.blackjack.is_winner())
