import random

class Game:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]
        self.hand = []

    def deal(self):
        self.hand.extend(self.pick_cards())

    def is_winner(self):
        return sum(i for i in self.hand) > 16

    def new_game(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]
        self.hand = []

    def pick_cards(self):
        card1 = random.choice(self.cards)
        self.remove_cards(card1)
        card2 = random.choice(self.cards)
        return [card1, card2]

    def remove_cards(self,card1):
        return self.cards.remove(card1)
