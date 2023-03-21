class GameBoard:
    def __init__(self, board_length: int, board_width: int) -> None:
        self.board_length = board_length
        self.board_width = board_width
        self.game_board = []
        self.game_positions = []
        self.guesses_made = []
        self.guesses_made_status = []

    def create_board(self, is_cpu=False, tracker=False) -> None:
        """
        Create a 2D array with a list of lists initialiazed with "0" as the placeholder
        """
        result = []
        len_of_board = []
        if tracker:
            for _ in range(self.board_width):
                len_of_board.append('O')
        else:
            for _ in range(self.board_width):
                len_of_board.append(0)
        for _ in range(self.board_length):
            result.append(len_of_board.copy())
        self.game_board = result
        if is_cpu is False:
            print('Your New Board: ')
            self.print_game_board()
    
    def add_piece(self, x_cor: int, y_cor: int, is_cpu=False) -> None:
        """
        Add a 1 on a board based on the provided x, y provided 
        """
        self.game_board[y_cor][x_cor] = 1
        if [y_cor, x_cor] not in self.game_positions:
            self.game_positions.append([y_cor, x_cor])
        if not is_cpu:
            self.print_game_board()

    def add_tracker(self, x_cor: int, y_cor: int) -> None:
        """
        Add a X on a board based on the provided x, y provided 
        """
        self.game_board[y_cor][x_cor] = 'X'
        self.print_game_board()
    
    def attack_piece(self, x_cor: int, y_cor: int, is_cpu=False) -> None:
        """
        If value present, add a X on a board based on the provided x, y
        and print the board to the user to indicate an attack was made
        """
        if [y_cor, x_cor] not in self.guesses_made:
            if self.game_board[y_cor][x_cor] == 1 and is_cpu:
                self.game_board[y_cor][x_cor] == 'X'
                self.game_positions.remove([y_cor, x_cor])
                print('I got you!')
            elif self.game_board[y_cor][x_cor] == 1 and not is_cpu:
                self.game_board[y_cor][x_cor] == 'X'
                self.game_positions.remove([y_cor, x_cor])
                print('You got me!')
            elif is_cpu:
                print('I missed!')
            else:
                print('You missed!')
            self.guesses_made_status.append([ x_cor + 1, y_cor + 1])
            self.guesses_made.append([y_cor, x_cor])
        elif not is_cpu:
            print('You have already guess that value - lose a turn')
        else:
            print('I guessed the same value and lost a turn...')
        if not is_cpu:
            print('As a reminder you have guessed: ')
            print(str(self.guesses_made_status))

    def is_game_over(self) -> bool:
        """
        Checks if the current game is over
        """
        if self.game_positions == []:
            return True
        else:
            return False

    def print_game_board(self) -> None:
        """
        Prints the current state of the game board
        """
        for line in self.game_board:
            str_value = str(line)
            removed_brackets = str_value[1:-1]
            str_value = removed_brackets.replace(',', '')
            print(str_value)

    if __name__ == '__main__':
        pass
