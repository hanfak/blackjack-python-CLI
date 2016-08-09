import unittest
from mock import MagicMock
import mock
from lib.game import Game

class TestUserStory(unittest.TestCase):
    def setUp(self):
        self.blackjack = Game()

    def test_user_story_0(self):
        """One player,two cards, number closest to 20 wins"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,8])
        self.blackjack.deal()
        self.assertTrue(self.blackjack.is_winner())

    def test_user_story_0(self):
        """restarts game with new deck and cleared hand"""
        self.blackjack.pick_cards = MagicMock(return_value=[10,8])
        self.blackjack.deal()
        self.blackjack.is_winner()
        self.blackjack.new_game()

        self.assertListEqual(self.blackjack.cards, [1,2,3,4,5,6,7,8,9,10])
        self.assertListEqual(self.blackjack.hand, [])
