import pygame
from constants import width, height, square_size, Black
from Board import board
from game import Game

# Start Program
pygame.init()

FPS = 60
# Screen
win = pygame.display.set_mode((width, height))

# Title and Icon
pygame.display.set_caption('Checkers')
icon = pygame.image.load('checkers.png')
pygame.display.set_icon(icon)
game = Game(win)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col

# Game Loop
running = True
while running:
    for event in pygame.event.get():

        if game.winner() != 0:
            print(game.winner())
            run = False

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)
            game.select(row, col)

    game.update()


