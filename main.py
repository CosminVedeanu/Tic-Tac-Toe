from Functii import player_input, choose_first, game, replay

print('Welcome to Tic Tac Toe!')

while True:

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' este primul! ')
    game_on = False

    play_game = input('Esti gata sa incepi jocul? Y/N ')

    if play_game.lower()[0] == 'y':
        game_on = True

    while game_on:
        if turn == 'Player 1':
        # Player 1 Turn
            game_on = game(turn, board, player1_marker)
            turn = 'Player 2'
        else:
        # Player2's turn.
            game_on = game(turn, board, player2_marker)
            turn = 'Player 1'

    if not replay():
        break