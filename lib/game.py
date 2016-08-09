import random

class Game:
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
        self.hand = []

    def deal(self):
        self.hand.extend(self.pick_cards())

    def points(self):
        self.hand = self.__change_ace_card()
        self.hand = self.__change_face_card()
        return sum(i for i in self.hand)

    def is_winner(self):
        return self.points() == 21

    def new_game(self):
        self.cards = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
        self.hand = []

    def pick_cards(self):
        card1 = random.choice(self.cards)
        self.__remove_cards(card1)
        card2 = random.choice(self.cards)
        return [card1, card2]

    def __remove_cards(self,card1):
        return self.cards.remove(card1)

    def __check_suit(self, card):
        return card == 'J' or card == 'Q' or card =='K'

    def __change_face_card(self):
        return [10 if self.__check_suit(card) else card for card in self.hand]

    def __change_ace_card(self):
        return [11 if card == 'A' else card for card in self.hand]
