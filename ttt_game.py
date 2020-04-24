import random
"""
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
"""

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player1 = ''
player2 = ''


def win_message(name):
    print('-' * 45)
    print(f'Congratulations! Player {name} won')
    print('-' * 45)


def display_board(game_board):
    """ function that can print out a board """
    print('-------------')
    print(f'| {game_board[1]} | {game_board[2]} | {game_board[3]} |')
    print('-------------')
    print(f'| {game_board[4]} | {game_board[5]} | {game_board[6]} |')
    print('-------------')
    print(f'| {game_board[7]} | {game_board[8]} | {game_board[9]} |')
    print('-------------')


def player_input():
    """ function that can take in a player input and
    assign their marker as 'X' or 'O' """
    global player1, player2
    while True:
        player_mark_choice = input('Player1, do you want to be "X" or "O"? ').upper()
        if player_mark_choice == 'X':
            player1, player2 = 'X', 'O'
            return player1, player2
        elif player_mark_choice == 'O':
            player1, player2 = 'O', 'X'
            return player1, player2
        else:
            print('Please specify X or O')
            continue


def place_marker(game_board, marker, position):
    """ function that takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board """
    game_board[position] = marker


def win_check(game_board, marker):
    """ function that takes in a board and a mark (X or O)
    and then checks to see if that mark has won """
    win_list = [game_board[1:4],
                game_board[4:7],
                game_board[7:10],
                game_board[1:10:4],
                game_board[3:8:2],
                game_board[1:8:3],
                game_board[2:9:3],
                game_board[3:10:3]]
    if [marker, marker, marker] in win_list:
        return True
    else:
        return False


def choose_first():
    """ function that uses the random module to randomly decide which player goes first.
    You may want to lookup random.randint() Return a string of which player went first """
    players = [player1, player2]
    return random.choice(players)


def space_check(game_board, position):
    """ function that returns a boolean indicating whether a space on the
    board is freely available """
    if game_board[position] == ' ':
        return True
    else:
        return False


def full_board_check(game_board):
    """ function that checks if the board is full and returns a boolean value.
    True if full, False otherwise """
    x = ' '
    if x in game_board:
        return False
    else:
        return True


def player_choice(game_board):
    """ function that asks for a player's next position (as a number 1-9)
    and then uses the function from step 6 to check if it's a free position.
    If it is, then return the position for later use """
    while True:
        try:
            player_next_turn = int(input('Choose your next position: (1-9): '))
            if not space_check(game_board, player_next_turn):
                print('This is occupied cell. Try again')
            else:
                return player_next_turn
        except ValueError:
            print('Please provide a number (1-9), not a string')
            continue
        except IndexError:
            print('Please provide a number from 1 to 9')
            continue


def replay():
    """ function that asks the player if they want to play again and
    returns a boolean True if they do want to play again """
    play_again = input('Play again? (y/n) ')
    if play_again == 'y':
        return True


while True:
    print('Welcome to Tic Tac Toe Game!')
    display_board(board)

    while True:
        place_marker(board, player1, player_choice(board))
        display_board(board)
        if win_check(board, player1):
            win_message(player1)
            board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            break
        elif full_board_check(board):
            display_board(board)
            print('Tie Game')
            break
        place_marker(board, player2, player_choice(board))
        display_board(board)
        if win_check(board, player2):
            win_message(player2)
            board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            break
        elif full_board_check(board):
            display_board(board)
            print('Tie Game')
            break
        continue

    if not replay():
        break
