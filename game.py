import pygame
from constants import White, Black, Blue, square_size
from Board import board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()


    def _init(self):
        self.selected = None
        self.board = board()
        self.turn = Black
        self.valid_moves = {}

    # Unfinished
    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    # Movement Recursion Loop
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    # Moving and Double Jumping
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    # Draws dots where valid moves are
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, Blue, (col * square_size + square_size//2, row * square_size + square_size//2), 15)

    # Changes Turns
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == Black:
            self.turn = White
        else:
            self.turn = Black