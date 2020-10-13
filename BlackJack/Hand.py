class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        if isinstance(card, list):
            self.aces += 1
        else:
            self.cards.append(card)
            self.value += card

    def adjust_for_ace(self):
        while self.aces > 0:
            if self.value + 11 > 21:
                self.value += 1
                self.cards.append(1)
            else:
                self.value += 11
                self.cards.append(11)
            self.aces -= 1
        return self.value
