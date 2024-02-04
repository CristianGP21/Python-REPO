import os
import random


def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board(board):
    clear_output()
    print('\n' + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    print(' +---+---+---+')
    print(' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print(' +---+---+---+')
    print(' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    return board


# test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# display_board(test_board)


def player_input():
    marker = ''

    # ASK Player 1 to choose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    # ASSIGN PLAYER 2, the opposite marker
    player1 = marker

    if marker == 'X':
        print('Player 1 will be X')
        print('Player 2 will be O')
        return ('X', 'O')
    else:
        print('Player 1 will be O')
        print('Player 2 will be X')
        return ('O', 'X')


# player_input()


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or  # Top Row
            (board[4] == board[5] == board[6] == mark) or  # Middle Row
            (board[1] == board[2] == board[3] == mark) or  # Bottom Row
            (board[7] == board[4] == board[1] == mark) or  # Left Column
            (board[8] == board[5] == board[2] == mark) or  # Middle Column
            (board[9] == board[6] == board[3] == mark) or  # Right Column
            (board[7] == board[5] == board[3] == mark) or  # Diagonal 1
            (board[9] == board[5] == board[1] == mark))    # Diagonal 2


# print(win_check(test_board, 'X'))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): '))
        if board[position] in ['X', 'O']:
            print('Position already taken. Pick another one!')

    return position


def replay():
    return input('Do you want to play again? \nEnter Yes or No: ').lower().startswith('y')


############################################################################################################
############################################################################################################

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    display_board(['#', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    theBoard = display_board([' '] * 10)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Are you ready to play? \nEnter Yes or No:')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # It is Player's 1 turn

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('It is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)


            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('It is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
