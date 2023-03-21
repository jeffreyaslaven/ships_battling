from game_board import GameBoard
from random import randrange
import time

"""
Core logic for Ships Battling
"""
class GameLogic:
    def __init__(self) -> None:
        pass

    def play_game(self, restart=False) -> bool:
        if restart:
            print ('Welcome back!')
            name = input('Could you remind what your name is? ')
        else:
            name = input('Hello there, what is your name? ')
            print("Hello " + name)

        play_game = input('Want to play a game of \"Ships Battling\"? It\'s TOTALLY not a knock-off of Battleship. Type \"Y\" for Yes and \"N\" for No: ')

        while play_game != 'Y' or play_game != 'y':
            if play_game == 'N' or play_game == 'n':
                print('Well okay, ' + name + ', bye for now!')
                break
            elif play_game == 'Y' or play_game == 'y':
                break
            play_game = input('I don\'t understand your input ' + name + '. Please either type "Y" or "N": ')

        """
        Creating the player board and gathering information from the user
        """
        if play_game == 'Y' or play_game == 'y':
            how_tall = input('Great to hear! How tall do you want the board?: ')
            while how_tall.isdigit() is False:
                if how_tall.isdigit():
                    break
                how_tall = input('That was not a valid input, please enter a valid number for the height of your game board: ')
            how_wide = input('How wide do you want the board?: ')
            while how_wide.isdigit() is False:
                if how_wide.isdigit():
                    break
                how_wide = input('That was not a valid input, please enter a valid number for the width of your game board: ')
            
            game = GameBoard(int(how_tall), int(how_wide))
            game.create_board()

            game_piece = input('Now it is time to add your game pieces. Please enter your pieces in coordinate format i.e. x, y: ')

            while game_piece.lower() != 'start':
                try:
                    game_piece_val = game_piece.strip()
                    game_piece_val = game_piece_val.split(',')
                    x_val = int(game_piece_val[0]) - 1
                    y_val = int(game_piece_val[1]) - 1
                    game.add_piece(x_val, y_val)
                    game_piece = input('Please enter another piece in coordinate format i.e. x, y or type "start" to begin: ')
                except IndexError:
                    game_piece = input('You entered an location outside of the board. Please enter another piece in coordinate format i.e. x, y or type "start" to begin: ')
                except Exception as e:
                    if game_piece.lower() == 'start':
                        break
                    game_piece = input('That is not a valid input. Please enter your pieces in coordinate format i.e. x, y or type "start" to begin: ')

            """
            Gathering information on how many 'boats' the CPU player should have
            """
            cpu_boats = input('How many boats do you want me to have?: ')
            while cpu_boats.isdigit() is False:
                if cpu_boats.isdigit():
                    if cpu_boats > how_wide * how_tall:
                        cpu_boats = input('Invalid value. You entered a number larger than what is possible on the board. How many boats do you want me to have?: ')
                    else:
                        break
                cpu_boats = input('Invalid value. Please enter a valid number. How many boats do you want me to have?: ')
            
            print('Great! I will have ' + cpu_boats + ' boats. Let me place them on my board.')

            """
            Creating the CPU player
            """
            cpu_positions = []
            cpu_game = GameBoard(int(how_tall), int(how_wide))
            cpu_game.create_board(True)
            tracking_board_cpu = GameBoard(int(how_tall), int(how_wide))
            tracking_board_cpu.create_board(True, True)

            """
            Placing specified number of CPU boats on the board
            """
            while len(cpu_positions) < int(cpu_boats):
                value = [randrange(int(how_tall)), randrange(int(how_wide))]
                if value not in cpu_positions:
                    cpu_game.add_piece(value[0], value[1], True)
                    cpu_positions.append(value)
        
            print('Let the games begin!')
            print('Just a reminder, this your board:')
            game.print_game_board()

            print('__________________________________________________')
            print('\n')

            tracking_board = GameBoard(int(how_tall), int(how_wide))
            tracking_board.create_board(True, True)

            """
            Checks game state of both boards to see if the game is over
            """
            def check_if_game_over() -> bool:
                if game.is_game_over() is True:
                    print('You lose! Try again')
                    return True
                elif cpu_game.is_game_over() is True:
                    print('You win!')
                    return True
                else:
                    return False
            
            """
            Start the battle between the CPU and player
            """
            while True:
                if check_if_game_over():
                    break
                user_turn = input('Your turn - enter a coordinate in coordinate format i.e. x,y: ')
                try:
                    user_turn_val = user_turn.strip()
                    user_turn_val = user_turn_val.split(',')
                    x_val = int(user_turn_val[0]) - 1
                    y_val = int(user_turn_val[1]) - 1
                    cpu_game.attack_piece(x_val, y_val)
                    tracking_board.add_tracker(x_val, y_val)
                except IndexError:
                    print('You entered an location outside of the board. Lose a turn!') 
                except Exception:
                    print('You entered an invalid value. Lose a turn!') 
                print('__________________________________________________')
                if check_if_game_over():
                    break
                cpu_value = [randrange(int(how_tall)), randrange(int(how_wide))]
                print('Thinking...')
                time.sleep(randrange(5))
                print('Let me try...')
                time.sleep(1)
                game.attack_piece(cpu_value[0], cpu_value[1], True)
                print('What I have tried:')
                tracking_board_cpu.add_tracker(cpu_value[0], cpu_value[1])
                print('__________________________________________________')
        
        """
        Check to see if the player wants restart the game
        """
        while True:
            player_decision = input('Do you want to play again? "Y" for yes, "N" for no: ')
            if player_decision.lower() != 'y' and player_decision.lower() != 'n':
                print('Invalid input. Please enter "Y" for yes or "N" for no.')
            elif player_decision.lower() == 'y':
                return True
            else:
                return False
        
    if __name__ == '__main__':
        pass        