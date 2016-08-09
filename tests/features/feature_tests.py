import unittest
from mock import MagicMock
import mock
from lib.game import Game

class TestUserStory(unittest.TestCase):
    def setUp(self):
        self.blackjack = Game()

    @mock.patch('random.choice')
    def test_user_story_1(self, random_call):
        """One player, numbers cards wins closest to 10"""
        random_call.return_value = 8
        self.assertTrue(self.blackjack.deal())
