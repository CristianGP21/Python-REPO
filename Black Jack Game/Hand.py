import Cards


class Hand():

    def __init__(self):
        self.cards = []  # Empty list to hold the cards
        self.value = 0  # Start with 0 Value
        self.aces = 0  # Keep track of aces

    def add_card(self, card):
        # from Deck.deal -> single card Object
        self.cards.append(card)
        self.value += Cards.values[card.ranks]  # Adjust the value with the card that was added

        if card.ranks == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # Change Ace value to 1 in case of Bust
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
