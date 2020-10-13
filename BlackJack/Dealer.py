from Hand import Hand


class Dealer(Hand):
    def show(self):
        self.adjust_for_ace()
        return self.cards[0]
