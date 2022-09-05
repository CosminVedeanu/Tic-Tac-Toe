from Functii import display_board, player_input, place_marker, win_check, choose_first,space_check, full_board_check, player_choice, game, replay

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
            game_on = game(turn, blackboard, player1_marker, game_on)
            turn = 'Player 2'
        else:
        # Player2's turn.
            game_on = game(turn, blackboard, player2_marker, game_on)
            turn = 'Player 1'

    if not replay():
        break