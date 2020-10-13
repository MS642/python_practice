import random

suits = ['Hearts', 'Spade', 'Diamond', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ace': [1, 11]}


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(values[rank])

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Have {len(self.all_cards)} cards left in the deck'

