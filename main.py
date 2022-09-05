from Functii import player_input, choose_first, game, replay

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here

    # feedback: blackboard' s variable name is not relevant to its use. Rename it with a more relevant name.
    # Try using refactor -> right click on variable -> refactor -> rename
    blackboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' este primul! ')

    play_game = input('Esti gata sa incepi jocul? Y/N ')

    # feedback: Instead of trying if/else you can directly assign to game_on the value of the if' s condition value
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