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

    @mock.patch('random.choice')
    def test_1(self, random_call):
        """Player dealt winning card"""
        random_call.return_value = 8
        self.assertTrue(self.blackjack.deal())

    @mock.patch('random.choice')
    def test_2(self, random_call):
        """Player dealt losing hand"""
        random_call.return_value = 3
        self.assertFalse(self.blackjack.deal())
