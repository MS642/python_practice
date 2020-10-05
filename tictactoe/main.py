from IPython.display import clear_output


def display_board(board):
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3])


def choose_first():
    player_1 = ''
    while player_1 != 'X' and player_1 != 'O':
        player_1 = input('Please Choose X or O: ')
    return ('X', 'O') if player_1 == 'X' else ('O', 'X')


def player_input():
    user_in = 'not'
    while not user_in.isdigit() or not int(user_in) in range(1, 10):
        user_in = input("Please enter the block you want to mark (1-9): ")
    return int(user_in)


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    test_1 = board[1] == mark and board[4] == mark and board[7] == mark
    test_2 = board[9] == mark and board[8] == mark and board[7] == mark
    test_3 = board[9] == mark and board[6] == mark and board[3] == mark
    test_4 = board[1] == mark and board[2] == mark and board[3] == mark
    test_5 = board[1] == mark and board[5] == mark and board[9] == mark
    test_6 = board[7] == mark and board[5] == mark and board[3] == mark
    test_7 = board[4] == mark and board[5] == mark and board[6] == mark
    test_8 = board[8] == mark and board[5] == mark and board[2] == mark
    return test_1 or test_2 or test_3 or test_4 or test_5 or test_6 or test_7 or test_8


def replay():
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input('Play again? Y/N: ')
    return choice == 'Y'


def player_choice(board):
    user_in = False
    while not user_in:
        user_in = player_input()
        print("please enter a valid position")
    return user_in if space_check(board, user_in) else player_choice(board)


def full_board_check(board):
    test_1 = board[7] != ' ' and board[8] != ' ' and board[9] != ' '
    test_2 = board[4] != ' ' and board[5] != ' ' and board[6] != ' '
    test_3 = board[1] != ' ' and board[2] != ' ' and board[3] != ' '
    return test_3 and test_2 and test_1


def space_check(board, position):
    return board[position] == ' '


replay_game = True
while replay_game:
    print('Welcome to Tic Tac Toe!')
    test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    (player_1, player_2) = choose_first()
    player_1_turn = True
    while not full_board_check(test_board):
        user_in = player_choice(test_board)
        marker = player_1 if player_1_turn else player_2
        print(player_1_turn)
        test_board = place_marker(test_board, marker, user_in)
        display_board(test_board)
        if win_check(test_board, marker):
            winner = 'Player 1' if player_1_turn else 'Player 2'
            print(f"Congratulations! {winner} is the winner!")
            break
        clear_output(True)
        player_1_turn = not player_1_turn
    print('Game Over!')
    if replay():
        continue
    else:
        replay_game = False
        break

print('Have a good day!')
