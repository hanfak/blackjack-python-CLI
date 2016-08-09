import unittest
from mock import MagicMock
import mock
from lib.game import Game

class TestUserStory(unittest.TestCase):
    def setUp(self):
        self.blackjack = Game()

    def test_user_story_1(self):
        """One player,two cards, number closest to 20 wins"""
        self.blackjack.pickCards = MagicMock(return_value=[10,8])
        self.blackjack.deal()
        self.assertTrue(self.blackjack.winner())
