import random
import Card


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in Card.suits:
            for rank in Card.ranks:
                # Create the Card Object
                created_card = Card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
