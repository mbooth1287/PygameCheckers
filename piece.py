from constants import White, Black, square_size, gray, crown
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = square_size * self.col + square_size // 2
        self.y = square_size * self.row + square_size // 2

    def make_king(self):
        self.king = True

    # Draws Piece
    def draw(self, win):
        radius = square_size // 2 - self.PADDING
        pygame.draw.circle(win, gray, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(crown, (self.x - crown.get_width()//2, self.y - crown.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return string(self.color)


