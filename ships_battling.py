from game_logic import GameLogic

play_ships_battling = GameLogic()

keep_playing_game = True
has_user_restart = False
while True:
    if keep_playing_game:
        keep_playing_game = play_ships_battling.play_game(has_user_restart)
        has_user_restart = True
    else:
        break


print('____________________')
print('\n')
print('Thanks for playing!')
print('Created By: Jeffrey Slaven')
print('\n')
print('____________________')