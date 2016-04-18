# coding=utf-8
from __future__ import print_function
from board import GameBoard

import random



class Game(object):
    def __init__(self):
        self.board = GameBoard()
        self.X = self.board.X
        self.O = self.board.O
        self.active_player = self.X

    @property
    def has_winner(self):
        return not self.find_winner() is None

    @property
    def current_player_name(self):
        return 'X' if self.active_player == self.X else 'O'

    @property
    def winner(self):
        if not self.has_winner:
            return "No winner"

        return 'X' if self.find_winner() == self.X else 'O'

    @property
    def get_available_moves(self):
        import numpy as np
        
        moves = np.argwhere(np.array(self.board.cells)==0).tolist()
        return moves

    def find_winner(self):
        board = self.board
        winner = None
        for i in range(3):
            sums = [
                board.cells[0][0] + board.cells[0][1] + board.cells[0][2],  # r1
                board.cells[1][0] + board.cells[1][1] + board.cells[1][2],  # r2
                board.cells[2][0] + board.cells[2][1] + board.cells[2][2],  # r3
                board.cells[0][0] + board.cells[1][0] + board.cells[2][0],  # c1
                board.cells[0][1] + board.cells[1][1] + board.cells[2][1],  # c2
                board.cells[0][2] + board.cells[1][2] + board.cells[2][2],  # c3
                board.cells[0][0] + board.cells[1][1] + board.cells[2][2],  # diag 1
                board.cells[0][2] + board.cells[1][1] + board.cells[2][0]  # diag 2
            ]

            if 3 in sums:
                winner = 'X'

            elif -3 in sums:
                winner = 'O'

        return winner

    def cell_already_played(self, row, col):
        return not self.board.cells[row][col] == self.board.empty

    def get_cell(self, row, col):
        return self.board.cells[row][col]

    def play_cell(self, row, col):
        self.board.cells[row][col] = self.active_player

    def switch_players(self):
        self.active_player = self.X if self.active_player == self.O else self.O
