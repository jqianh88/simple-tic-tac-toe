import math 
import random


class Player(object):
    def __init__(self, player_letter: str):
      self.player_letter = player_letter

    def get_move(self, game, board_size: int):
      pass


class RandomComputerPlayer(Player):
    def __init__(self, player_letter: str):
      super().__init__(player_letter)

    def get_move(self, game, board_size: int):
        board = random.choice(game.available_moves())
        return board

class HumanPlayer(Player):
    def __init__(self, player_letter: str):
      super().__init__(player_letter)

    def get_move(self, game, board_size: int):
        valid_board = False
        val = None
        while not valid_board: 
            board = input(self.player_letter + f"\'s turn. Input move (0-{str(board_size * board_size)}): ")
            try: 
                val = int(board)
                if val not in game.available_moves(): 
                    raise ValueError
                valid_board = True 
            except ValueError: 
                print("Invalid selection. Try again")
        return val
        
        



