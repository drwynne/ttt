# coding=utf-8
from __future__ import print_function


class GameBoard(object):
    def __init__(self):
        self.X = 1
        self.O = -1
        self.empty = 0
        self.cells = self.initialize_board()

    def initialize_board(self):
        cells = [
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty],
            [self.empty, self.empty, self.empty]
        ]
        return cells

    def print_board(self):
        str_dict = {self.X: 'X',
                    self.O: 'O',
                    self.empty: '.'}

        text = '-----\n'.join(['{}\n'.format('|'.join([str_dict[j] for j in i])) for i in self.cells])

        return text

    def __str__(self):
        return self.print_board()
