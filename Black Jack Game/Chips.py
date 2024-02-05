class Chips():

    def __init__(self,total = 100):
        self.total = total      # Default value - Can be changed by user input
        self.bet = 0            # Will be changed according to user input

    def win_bet(self):
        self.total += self.bet
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        return self.total