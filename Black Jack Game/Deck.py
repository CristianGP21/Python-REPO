import random
import Cards


class Deck():

    def __init__(self):
        # Create the Deck from the Cards object
        self.deck = []
        for suit in Cards.suits:
            for rank in Cards.ranks:
                self.deck.append(Cards.Cards(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        # Doesn't return anything, just shuffle's the Deck
        random.shuffle(self.deck)

    def deal(self):
        # Remove one card from the list of all_cards
        return self.deck.pop()



