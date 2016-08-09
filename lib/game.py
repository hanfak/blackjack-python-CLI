import random

class Game:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]

    def deal(self):
        return random.choice(self.cards) > 6
