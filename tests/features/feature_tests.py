import unittest
from mock import MagicMock
import mock
from lib.game import Game

class TestUserStory(unittest.TestCase):
    def setUp(self):
        self.blackjack = Game()

    def test_user_story_0a(self):
        """_One player two cards number closest to 20 wins"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,9])
        self.blackjack.deal()
        self.assertEqual(self.blackjack.points(), 19)

    def test_user_story_0b(self):
        """_restarts game with new deck and cleared hand"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,'Q'])
        self.blackjack.deal()
        self.blackjack.points()
        self.blackjack.new_game()

        self.assertListEqual(self.blackjack.cards, [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K','A'])
        self.assertListEqual(self.blackjack.hand, [])

    def test_user_story_0c(self):
        """_Play game with face card"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,'Q'])
        self.blackjack.deal()

        self.assertEqual(self.blackjack.points(), 20)

    def test_user_story_0d(self):
        """_Play game with ace card"""
        self.blackjack.pick_cards = MagicMock(return_value=['A','Q'])
        self.blackjack.deal()

        self.assertTrue(self.blackjack.is_winner())
