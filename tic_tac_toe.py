

import time
from players import HumanPlayer, RandomComputerPlayer


class TicTacToe(object):

    def __init__(self):
        # n = 9
        # self.spots = {i:f'{i}' for i in range(1,n+1)}
        # self.tic_tac_toe_board = "".join([f'|{self.spots[i]}' if i % 3 != 0 else f'|{self.spots[i]}|\n' for i in range(1,n+1)])
        self.board_size = 3
        self.tic_tac_toe_board = [' ' for _ in range(self.board_size*self.board_size)]
        self.current_winner = None

    def print_board(self, board_size: int):

        # To get the rows 
        for row in [self.tic_tac_toe_board[i*board_size:(i+1)*board_size] for i in range(board_size)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums(board_size: int): 
        number_board = [[str(i) for i in range(j*board_size, (j+1)*board_size)] for j in range(board_size)]
        for row in number_board: 
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self) -> list[int]:
        return [i for i, spot in enumerate(self.tic_tac_toe_board) if spot == ' ']


    def empty_spots(self) -> list:
        return ' ' in self.tic_tac_toe_board
    
    def num_empty_spots(self) -> int: 
        return len(self.tic_tac_toe_board.count(' '))
           
    def make_move(self, spot: str, letter: str, board_size: int) -> bool: 
        if self.tic_tac_toe_board[spot] == ' ':
            self.tic_tac_toe_board[spot] = letter
            if self.is_winner(spot, letter, board_size=board_size): 
                self.current_winner = letter

            return True
        return False

    def is_winner(self, spot: str, letter: str, board_size: int): 
        # All conditions of when a person wins
        row_index = spot // board_size
        row = self.tic_tac_toe_board[row_index*board_size : (row_index + 1) * board_size]
        if all([el==letter for el in row]):
            return True 
        
        column_index = spot % board_size
        # TODO Have to fix this for larger board_sizes.
        column = [self.tic_tac_toe_board[column_index+i*board_size] for i in range(board_size)]
        if all([el==letter for el in column]):
            return True 
        if spot % (board_size-1) == 0: 
            left_diagonal_list = [i for i in range(board_size * board_size) if i % (board_size+1) == 0]
            left_diagonal = [self.tic_tac_toe_board[i] for i in left_diagonal_list]
            if all ([el==letter for el in left_diagonal]):
                return True 
            
            right_diagonal_list = [i for i in range(board_size * board_size) if i % (board_size-1) == 0]
            right_diagonal = [self.tic_tac_toe_board[i] for i in right_diagonal_list]
            if all ([el==letter for el in right_diagonal]):
                return True 


def play(game, x_player, o_player, print_game=True, board_size=3):
    # returns the winner of the game or None for a tie
    if print_game: 
        game.print_board_nums(board_size=board_size)

    player_letter = 'X'
    
    # Iterate until the game finishes (winner or tie)
    while game.empty_spots():
        # Get each player's move
        if player_letter == 'O':
            spot = o_player.get_move(game, board_size=board_size)
        else: 
            spot = x_player.get_move(game, board_size=board_size)

        if game.make_move(spot=spot, letter=player_letter, board_size=board_size):
            if print_game: 
                print(player_letter + f' makes a move to {spot=}')
                game.print_board(board_size=board_size)
                print('')
            
            if game.current_winner and print_game:
                print(player_letter + ' wins!') 
                return player_letter

            # Alternate players 
            player_letter = 'O' if player_letter == 'X' else 'X'

        time.sleep(0.9)
    if print_game: 
        print("It's a tie! Play another round!")
       
        
if __name__=='__main__':

    board_size = 3
    x_player = HumanPlayer(player_letter='X')
    o_player = RandomComputerPlayer(player_letter='O')

    game = TicTacToe()
    play(game, x_player=x_player, o_player=o_player, print_game=True, board_size=board_size)