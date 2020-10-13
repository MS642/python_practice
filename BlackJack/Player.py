from Hand import Hand


class Player(Hand):
    def show(self):
        return self.adjust_for_ace()
