import os
import random

def display_board(board):
    os.system('cls')  # on windows
    #print('\n'*100)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

#test_board = ['#','X',' ','X','O','X','O','X','O','X']
#test_board = ['']*10
#display_board(test_board)


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Jucator 1:Vrei X sau O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


#player_input()



def place_marker(board, marker, position):
    board[position] = marker

#place_marker(test_board,'$',5)
#display_board(test_board)


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark)  # orizonat 1
            or (board[4] == mark and board[5] == mark and board[6] == mark)  # orizontal 2
            or (board[1] == mark and board[2] == mark and board[3] == mark)  # orizontal 3
            or (board[7] == mark and board[4] == mark and board[1] == mark)  # vertical 1
            or (board[8] == mark and board[5] == mark and board[2] == mark)  # vertical 2
            or (board[9] == mark and board[6] == mark and board[3] == mark)  # vertical 3
            or (board[1] == mark and board[5] == mark and board[9] == mark)  # digonal 1
            or (board[7] == mark and board[5] == mark and board[3] == mark)  # diagonal 2
            )

#win_check(test_board,'X')

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
            if space_check(board, position) == False:
                print("Pozitia este ocupata, alege alta pozitie")
        except:
            print("Te rog sa introduci o valoare valida! ")

    return position

def game(turn, board, player_marker):
    display_board(board)
    position = player_choice(board)
    place_marker(board, player_marker, position)

    if win_check(board, player_marker):
        display_board(board)
        print(turn + ' a câstigat! ')
        return False
    else:
        if full_board_check(board):
            display_board(board)
            print('Jocul se termina ca remiza! ')
            return False
    return True
def replay():
    return input('Daca vrei sa joci din nou sa joci din nou introdu orice valoare daca nu apasa ENTER')

