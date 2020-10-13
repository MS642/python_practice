from Deck import Deck
from Chips import Chips
from Dealer import Dealer
from Player import Player


def take_bet(current_chips):
    ask = True
    bet = 0
    while ask:

        bet = input('What is your bet? ')
        if bet.isdigit() and int(bet) <= current_chips:
            ask = False
        else:
            print('Please enter a valid bet')
    print(f'player bet {bet}')
    return int(bet)


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    return hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    ask = True
    hit_stand = ''
    while ask:
        hit_stand = input('Do you want to hit? Y/N ')
        if hit_stand == 'Y' or hit_stand == 'N':
            ask = False
        else:
            print('Invalid Input')
    if hit_stand == 'N':
        playing = False
    else:
        hit(deck, hand)


def show_some(player, dealer):
    print(f'Player has total value {player.show()}')
    print(f'Dealer card value is {dealer.show()}')
    return player.show(), dealer.show()


def show_all(player, dealer):
    print(f'Player has {player.adjust_for_ace()}')
    print(f'Dealer has {dealer.adjust_for_ace()}')
    return player.adjust_for_ace(), dealer.adjust_for_ace()


if __name__ == '__main__':
    chip = ''
    while not chip.isdigit():
        chip = input('How many chips do you have? ')
    chips = Chips(int(chip))
    player = Player()
    dealer = Dealer()
    player.chips = 200
    while True:
        print(f'Your total Chips is {chips.total}')
        deck = Deck()
        deck.shuffle()
        player.cards = []
        dealer.cards = []
        player.value = 0
        dealer.value = 0
        bet = 0
        bet += take_bet(chips.total - bet)
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        show_some(player, dealer)
        playing = True
        while playing:
            hit_or_stand(deck, player)
            show_some(player, dealer)
            if player.adjust_for_ace() > 21:
                print('Player is a Bust')
                break
        show_all(player, dealer)
        while dealer.adjust_for_ace() < 17 and player.adjust_for_ace() <= 21:
            hit(deck, dealer)
            show_all(player, dealer)
        if player.adjust_for_ace() < dealer.adjust_for_ace() <= 21 or player.adjust_for_ace() > 21:
            chips.lose_bet(bet)
            print(f'Dealer Won! You lost {bet}')
        else:
            chips.win_bet(bet)
            print(f'Congratulations! You won {bet*2}, Your total is {chips.total}')
        if input('Play again? Y? ') != 'Y':
            break