# coding=utf-8
from __future__ import print_function

from game import Game
import os
import random

try:
    input = raw_input
except NameError:
    pass


class Program(object):
    def __init__(self, game_play='two_player'):
        self.game = Game()
        if game_play not in ['two_player', 'dumb', 'ai']:
            raise ValueError
        self.game_play = game_play


    def run(self):
        game = self.game
        board = game.board

        _ = os.system('cls')
        
        print('Welcome to Tic-Tac-Toe\n{}'.format('=' * 22))

        while not game.has_winner:
            print("""It's {}'s turn.""".format(game.current_player_name))

            if self.game_play == 'two_player' or game.active_player == game.X:
                row, col = self.get_position()
            
                # Validate position is not already taken
                if game.cell_already_played(row, col):
                    print('Try again. That position is occupied')
                    board.show()
                    continue

            else:
                row, col = random.choice(game.get_available_moves)
                print('{} plays: {},{}'.format(game.current_player_name, row, col))

            game.play_cell(row, col)
            board.show()

            game.switch_players()

        print('Winner is {}!'.format(game.find_winner()))
        board.show()


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


