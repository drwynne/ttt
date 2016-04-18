# coding=utf-8
from __future__ import print_function

from game import Game
import os

try:
    input = raw_input
except NameError:
    pass


class Program(object):
    def __init__(self):
        self.game = Game()

    def run(self):
        game = self.game
        board = game.board

        _ = os.system('cls')
        
        print('Welcome to Tic-Tac-Toe\n{}'.format('=' * 22))

        while not game.has_winner:
            print("""It's {0}'s turn.""".format(game.current_player_name))

            # Get position from player
            row, col = self.get_position()

            # Validate position is not already taken
            if game.cell_already_played(row, col):
                print('Try again. That position is occupied')
                print(board, end='\n')
                continue

            # Use cell
            game.play_cell(row, col)

            print(board)

            game.switch_players()

        print('Winner is {}!'.format(game.find_winner()))
        print(board)


    def get_position(self):
        """Get position from user input. Should be in format x,y"""

        while True:
            placement = input('Enter row, column: ')
            try:
                row, col = [int(i) for i in placement.strip().split(',')]
                if max(row, col) > 2:
                    raise IndexError
                break
            except (ValueError, IndexError):
                print('Please use format 1,1')

        _ = os.system('cls')

        return row, col


