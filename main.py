from Functii import player_input, choose_first,  game, replay

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here

    blackboard = [' '] * 10
    player1_marker, player2_marker = player_input()  # de verificat valoarea returnata
    turn = choose_first()
    print(turn + ' este primul! ')

    play_game = input('Esti gata sa incepi jocul? Y/N ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
        # Player 1 Turn
            game_on = game(turn, blackboard, player1_marker)
            turn = 'Player 2'
        else:
        # Player2's turn.
            game_on = game(turn, blackboard, player2_marker)
            turn = 'Player 1'

    if not replay():
        break