import os
import random

def display_board(board):
    os.system('cls')  # on windows

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Jucator 1:Vrei X sau O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark)
            or (board[4] == mark and board[5] == mark and board[6] == mark)
            or (board[1] == mark and board[2] == mark and board[3] == mark)
            or (board[7] == mark and board[4] == mark and board[1] == mark)
            or (board[8] == mark and board[5] == mark and board[2] == mark)
            or (board[9] == mark and board[6] == mark and board[3] == mark)
            or (board[1] == mark and board[5] == mark and board[9] == mark)
            or (board[7] == mark and board[5] == mark and board[3] == mark)
            )

def choose_first():
    if random.randint(1, 2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for position in range(1, 10):
        if space_check(board, position):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Alege o pozitie de la 1 la 9: '))
            if not space_check(board, position):
                print("Pozitia este ocupata, alege alta pozitie")
        except IndexError:
            print("Te rog sa introduci o valoare de la 1 la 9! ")
        except ValueError:
            print("Te rog sa introduci o valoare valida, o cifra de la 1 la 9! ")
    return position

def game(turn, board, player_marker):
    display_board(board)
    position = player_choice(board)
    place_marker(board, player_marker, position)

    if win_check(board, player_marker):
        display_board(board)
        print('\n' + turn + ' a câstigat! \n')
        return False
    else:
        if full_board_check(board):
            display_board(board)
            print('Jocul se termina ca remiza! ')
            return False
    return True
def replay():

    return input('Pentru a juca din nou introduce orice valoare.\nDaca nu mai doresti sa continui, apasa ENTER.\n')
