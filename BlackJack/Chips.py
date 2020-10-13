class Chips:
    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bet(self, bet):
        self.total += bet * 2

    def lose_bet(self, bet):
        self.total -= bet
