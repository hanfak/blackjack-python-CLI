import random

class Game:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]
        self.hand = []

    def deal(self):
        self.hand.extend(self.pickCards())

    def winner(self):
        return sum(i for i in self.hand) > 16

    def pickCards(self):
        card1 = random.choice(self.cards)
        self.removeCards(card1)
        card2 = random.choice(self.cards)
        return [card1, card2]

    def removeCards(self,card1):
        return self.cards.remove(card1)
