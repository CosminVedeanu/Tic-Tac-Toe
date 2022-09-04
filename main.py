from Functii import display_board, player_input, place_marker, win_check, choose_first,space_check, full_board_check, player_choice, replay

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    # pass

    blackboard = [' '] * 10
    player1_marker, player2_marker = player_input()  # de verificat valoarea returnata
    turn = choose_first()
    print(turn + ' este primul')

    play_game = input('Esti gata sa incepi jocul? Y/N')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
        # Player 1 Turn
            display_board(blackboard)
            position = player_choice(blackboard)
            place_marker(blackboard, player1_marker, position)

            if win_check(blackboard, player1_marker):
                display_board(blackboard)
                print('Player 1 a câstigat!')
                game_on = False
            else:
                if full_board_check(blackboard):
                    display_board(blackboard)
                    print('Jocul se termina ca remiza!')
                    break
                else:
                    turn = 'Player 2'
        else:
        # Player2's turn.

            display_board(blackboard)
            position = player_choice(blackboard)
            place_marker(blackboard, player2_marker, position)

            if win_check(blackboard, player2_marker):
                display_board(blackboard)
                print('Player 2 a câstigat!')
                game_on = False
            else:
                if full_board_check(blackboard):
                    display_board(blackboard)
                    print('Jocul se termina ca remiza!')
                    break
                else:
                    turn = 'Player 1'
    # pass

    if not replay():
        break